import cv2, torch, numpy as np, os
from mobile_sam import sam_model_registry, SamPredictor

# =========================================================
# CONFIGURACIÓN
# =========================================================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print("Usando dispositivo:", DEVICE)

# Rutas
output_dir = "outputs_sam"
os.makedirs(output_dir, exist_ok=True)

sam_checkpoint = "/home/ealchat/Documentos/Aula/Deep_Learning/models/mobile_sam.pt"
sam = sam_model_registry["vit_t"](checkpoint=sam_checkpoint)
sam.to(device=DEVICE)
sam.eval()
predictor = SamPredictor(sam)

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    raise RuntimeError("❌ No se pudo abrir la cámara.")

# =========================================================
# CAPTURA Y PROCESAMIENTO
# =========================================================
n_frames = 10
for i in range(n_frames):
    ret, frame = cap.read()
    if not ret:
        print("❌ Error al capturar frame.")
        break

    # Preprocesar
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (512, 512))

    torch.cuda.empty_cache()

    # --- Segmentación SAM ---
    predictor.set_image(frame_resized)
    masks, _, _ = predictor.predict(
        point_coords=None,
        point_labels=None,
        box=np.array([[0, 0, frame_resized.shape[1], frame_resized.shape[0]]]),
        multimask_output=False
    )

    if masks is not None and len(masks) > 0:
        mask = masks[0].astype("uint8") * 255
        mask_resized = cv2.resize(mask, (frame.shape[1], frame.shape[0]))

        colored_mask = np.zeros_like(frame)
        for c in range(3):
            colored_mask[:, :, c] = mask_resized * (0, 255, 0)[c] // 255

        blended = cv2.addWeighted(frame, 0.6, colored_mask, 0.4, 0)

        # Guardar imágenes
        cv2.imwrite(os.path.join(output_dir, f"frame_{i+1:02d}.jpg"), blended)
        cv2.imwrite(os.path.join(output_dir, f"mask_{i+1:02d}.png"), mask_resized)
        print(f"✅ Frame {i+1} segmentado y guardado.")
    else:
        print(f"⚠️ Frame {i+1}: SAM no generó máscara.")

cap.release()
print(f"\n🎯 Proceso completado. Resultados guardados en: {output_dir}")
