import os
import json

def convert_to_yolo_format(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    img_width = data['size']['width']
    img_height = data['size']['height']
    yolo_annotations = []

    for obj in data['objects']:
        class_id = obj['classId']
        points = obj['points']['exterior']
        x_min, y_min = points[0]
        x_max, y_max = points[1]

        # Calcular centro, ancho y altura
        x_center = (x_min + x_max) / 2 / img_width
        y_center = (y_min + y_max) / 2 / img_height
        width = (x_max - x_min) / img_width
        height = (y_max - y_min) / img_height

        yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")
    
    return yolo_annotations

trainDataPath = "datasets/"

os.makedirs(trainDataPath+"labels", exist_ok=True)

for img in os.listdir(trainDataPath+"train"):
    imgJson = trainDataPath+"imgsInf/"+img+".json"

    # Convert annotations
    yoloInf = convert_to_yolo_format(imgJson)

    imgTxt = trainDataPath+"labels/"+img+".txt"
    
    # Save annotations to file
    with open(imgTxt, 'w') as f:
        f.write('\n'.join(yoloInf))

print("We redy")