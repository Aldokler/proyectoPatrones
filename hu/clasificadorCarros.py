import os
import json
import numpy as np
import math
import cv2 as cv

estadisticos = []

def cargarEstadisticas(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r') as file:
                medias = [float(num) for num in file.readline().split()]
                varianzas = [float(num) for num in file.readline().split()]
            estadisticos.append((medias, varianzas))

def momentoHu(img):
    moments = cv.moments(img)
    huMoments = cv.HuMoments(moments)
    return huMoments.flatten()

def distancia_euclidiana(hist, media, varianza):
    """
    Calcula la distancia euclidiana entre el histograma dado y la media/varianza proporcionada.
    """
    hist = np.array(hist)
    media = np.array(media)
    return np.sqrt(np.sum((hist - media) ** 2 / varianza))

def analizarDigito(imagen, estadistico):
    """
    Funcion que analiza una imagen usando su histograma con un modelo estadistico
    el modelo estadistico es el mismo calculado en modeloEstadisticoPorDigito
    devuelve la distancia calculada para cada x que servira como parametro segun el umbral

    """
    
    momentoImagen = momentoHu(imagen)
    media = estadistico[0] 
    var = estadistico[1]
    distancia = distancia_euclidiana(momentoImagen, media, var)
    return distancia

def clasificar(imagen):
    lista = []
    for i in range(len(estadisticos)):
        analisis = analizarDigito(imagen, estadisticos[i])
        lista.append(analisis)
    return lista

modelos = ["bus", "car", "motorbike", "threewheel", "truck", "van"]
cargarEstadisticas("estadistico")
resultados = []

for i in os.listdir("../datasets/valid"):
    test = False

    img = cv.imread("../datasets/valid/"+i, cv.IMREAD_GRAYSCALE)

    tipo = modelos[np.argmin(clasificar(img))]

    imgJson = "../Vehicle-dataset/valid/ann/"+i+".json"
    with open(imgJson, 'r') as f:
        data = json.load(f)
    
    for obj in data['objects']:
        class_id = obj['classTitle']
        if class_id == tipo:
            test = True
            break
    
    resultados.append(test)

print(f'Porcentaje de que la pegó: {resultados.count(True)*100/len(resultados)}')

imagen = cv.imread("1KK1PZ28Q72R.jpg", cv.IMREAD_GRAYSCALE)
L = clasificar(imagen)
print(modelos[np.argmin(L)])


