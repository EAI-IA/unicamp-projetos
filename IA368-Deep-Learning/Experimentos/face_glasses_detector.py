import cv2, torch
from ultralytics import YOLO
from transformers import AutoImageProcessor, AutoModelForImageClassification
import numpy as np

# -------------------- CONFIG --------------------
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print("Usando:", DEVICE)

# Modelo de rostro
yolo_face = YOLO("yolov8n-face.pt")

# Clasificador de lentes
proc = AutoImageProcessor.from_pretrained("alireza7/glasses-classifier")
model = AutoModelForImageClassification.from_pretrained("alireza7/glasses-classifier").to(DEVICE)

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    raise RuntimeError("No se pudo abrir la cámara")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --- Detección de rostro ---
    results = yolo_face(frame, verbose=False)[0]
    boxes = results.boxes

    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        roi = frame[y1:y2, x1:x2]
        if roi.size == 0:
            continue

        # --- Clasificación ---
        img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        inputs = proc(images=img, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            logits = model(**inputs).logits
            pred = logits.argmax(-1).item()
        label = "Con Lentes" if pred == 1 else "Sin Lentes"

        color = (0,255,0) if pred==1 else (0,0,255)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("Detección de Lentes", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
