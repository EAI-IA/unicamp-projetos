import cv2, torch, numpy as np, random, time
from ultralytics import YOLO
from mobile_sam import sam_model_registry, SamPredictor

# =========================================================
# CONFIG
# =========================================================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print("Usando dispositivo:", DEVICE)

# Modelos
yolo_pose = YOLO("yolov8n-pose.pt")   # keypoints
sam_checkpoint = "/home/ealchat/Documentos/Aula/Deep_Learning/models/mobile_sam.pt"
sam = sam_model_registry["vit_t"](checkpoint=sam_checkpoint)
sam.to(device=DEVICE).eval()
predictor = SamPredictor(sam)

# Cámara
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    raise RuntimeError("❌ No se pudo abrir la cámara.")

COLORS = [tuple(random.randint(50,255) for _ in range(3)) for _ in range(25)]

# =========================================================
# LOOP PRINCIPAL
# =========================================================
while True:
    start = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    # --- YOLO Pose ---
    pose_results = yolo_pose(frame, verbose=False)[0]
    people = pose_results.boxes
    kps = pose_results.keypoints

    for i, box in enumerate(people):
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        roi = frame[y1:y2, x1:x2]
        if roi.size == 0:
            continue

        # 🔹 SAM segmenta región del cuerpo detectada
        roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        roi_small = cv2.resize(roi_rgb, (320, 320))
        predictor.set_image(roi_small)

        masks, _, _ = predictor.predict(
            point_coords=None,
            point_labels=None,
            box=np.array([[0, 0, roi_small.shape[1], roi_small.shape[0]]]),
            multimask_output=False
        )

        if masks is None or len(masks) == 0:
            continue

        mask_resized = cv2.resize(
            masks[0].astype("uint8") * 255,
            (roi.shape[1], roi.shape[0])
        )

        color = COLORS[i % len(COLORS)]
        colored_mask = np.zeros_like(roi)
        for c in range(3):
            colored_mask[:, :, c] = mask_resized * color[c] // 255

        blended = cv2.addWeighted(roi, 0.6, colored_mask, 0.4, 0)
        frame[y1:y2, x1:x2] = blended

        # 🔹 Keypoints sobre la persona
        if kps is not None and i < len(kps.data):
            keypoints = kps.data[i].cpu().numpy().reshape(-1, 3)
            for (x, y, p) in keypoints:
                if p > 0.5:  # confianza mínima
                    cv2.circle(frame, (int(x), int(y)), 3, (0,255,255), -1)

        # Etiqueta persona
        label = f"Persona {i+1} ({conf:.2f})"
        cv2.rectangle(frame, (x1, y1 - 25), (x1 + 160, y1), color, -1)
        cv2.putText(frame, label, (x1 + 5, y1 - 7),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

    # --- FPS ---
    fps = 1.0 / (time.time() - start)
    cv2.putText(frame, f"FPS: {fps:.1f}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("YOLOv8-Pose + SAM-Tiny", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
