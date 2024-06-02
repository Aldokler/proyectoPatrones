import numpy as np
import cv2 as cv
import os
import json
import math

trainDataPath = "datasets/"

for img in os.listdir(trainDataPath+"train"):
    imgJson = trainDataPath+"imgsInf/"+img+".json"

    imagen = cv.imread(trainDataPath+"train/"+img, cv.IMREAD_GRAYSCALE)

    with open(imgJson, 'r') as f:
        imgData = json.load(f)

    for obj in imgData['objects']:
        points = obj['points']['exterior']
        x_min, y_min = points[0]
        x_max, y_max = points[1]

        objeto = imagen[y_min:y_max, x_min:x_max]

        dataModel = cv.HuMoments(cv.moments(objeto))
        
        with open(obj['classTitle']+"Model.txt", 'a+') as f:
            for hu in dataModel:
                f.write(str(hu[0]) + ' ')
            f.write('\n')
    
print("We redy")