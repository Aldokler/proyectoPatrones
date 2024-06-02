from ultralytics import YOLO
import cv2 as cv
import numpy as np

# Cargar el modelo entrenado
model = YOLO('runs/detect/train6/weights/best.pt')  # Ajusta la ruta según sea necesario

# Realizar inferencia en una imagen nueva
image_path = 'pista.jpg'  # Ajusta la ruta de la imagen
results = model(image_path)
image = cv.imread(image_path)

for result in results:
    boxes = result.boxes.xyxy.cpu().numpy()  # Coordenadas de las cajas
    scores = result.boxes.conf.cpu().numpy()  # Puntuaciones de confianza
    class_ids = result.boxes.cls.cpu().numpy()  # IDs de clase

    for box, score, class_id in zip(boxes, scores, class_ids):
        x1, y1, x2, y2 = map(int, box)
        cv.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f'{model.names[int(class_id)]}: {score:.2f}'
        cv.putText(image, label, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Mostrar la imagen con OpenCV
cv.imshow('Detections', image)
cv.waitKey(0)
cv.destroyAllWindows()