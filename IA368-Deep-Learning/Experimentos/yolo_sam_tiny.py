import cv2, torch, numpy as np, time, random
from ultralytics import YOLO
from segment_anything import sam_model_registry, SamPredictor
from mobile_sam import sam_model_registry, SamPredictor
import time

# ==================== CONFIGURACIÓN ====================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print("Usando dispositivo:", DEVICE)

# Modelos
yolo_model = YOLO("yolov8n-seg.pt")             # detección rápida
# sam_checkpoint = "/home/ealchat/Documentos/Aula/Deep_Learning/models/sam2_tiny.pth"         # tu modelo Tiny
# sam = sam_model_registry["vit_t"](checkpoint=sam_checkpoint)

sam_checkpoint = "/home/ealchat/Documentos/Aula/Deep_Learning/models/sam_vit_b_01ec64.pth"
sam = sam_model_registry["vit_t"](checkpoint="/home/ealchat/Documentos/Aula/Deep_Learning/models/mobile_sam.pt")
# sam = sam_model_registry["vit_b"](checkpoint=sam_checkpoint)

sam.to(device=DEVICE)
predictor = SamPredictor(sam)

# ==================== FUENTE: CÁMARA ====================
cap = cv2.VideoCapture(1)   # cambia a 0 si usas la cámara integrada

if not cap.isOpened():
    raise RuntimeError("❌ No se pudo abrir la cámara.")


# Paleta de colores aleatorios
COLORS = [tuple(random.randint(0,255) for _ in range(3)) for _ in range(20)]


sam.eval()  # 🔹 Asegura modo evaluación

while True:
    start = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    # --- Detección con YOLO ---
    results = yolo_model(frame, verbose=False)[0]
    boxes = [b for b in results.boxes if int(b.cls[0]) == 0]  # solo personas

    # --- Segmentación SAM por persona ---
    for i, box in enumerate(boxes):
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # 🔹 Aumentar margen para darle contexto a SAM
        margin = 40
        x1 = max(0, x1 - margin)
        y1 = max(0, y1 - margin)
        x2 = min(frame.shape[1], x2 + margin)
        y2 = min(frame.shape[0], y2 + margin)

        roi = frame[y1:y2, x1:x2]
        if roi.size == 0:
            continue

        torch.cuda.empty_cache()

        # 🔹 Convertir color y mantener buena resolución
        roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        roi_resized = cv2.resize(roi_rgb, (512, 512))

        predictor.set_image(roi_resized)

        # 🔹 Prompt explícito: toda el área
        masks, _, _ = predictor.predict(
            point_coords=None,
            point_labels=None,
            box=np.array([[0, 0, roi_resized.shape[1], roi_resized.shape[0]]]),
            multimask_output=False
        )

        if masks is None or len(masks) == 0:
            continue

        # 🔹 Escalar máscara al tamaño original del ROI
        mask_resized = cv2.resize(
            masks[0].astype("uint8") * 255,
            (roi.shape[1], roi.shape[0])
        )

        # --- Coloración y mezcla ---
        color = COLORS[i % len(COLORS)]
        colored_mask = np.zeros_like(roi)
        for c in range(3):
            colored_mask[:, :, c] = mask_resized * color[c] // 255

        blended = cv2.addWeighted(roi, 0.6, colored_mask, 0.4, 0)
        frame[y1:y2, x1:x2] = blended

        # --- Etiqueta ---
        label = f"Persona {i+1} ({conf:.2f})"
        cv2.rectangle(frame, (x1, y1 - 25), (x1 + 150, y1), color, -1)
        cv2.putText(frame, label, (x1 + 5, y1 - 7),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

    # --- FPS ---
    fps = 1.0 / (time.time() - start)
    cv2.putText(frame, f"FPS: {fps:.1f}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("YOLO + MobileSAM + Etiquetas", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
