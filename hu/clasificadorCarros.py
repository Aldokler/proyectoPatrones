import os
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
    return [-1 * math.copysign(1.0, hu) * math.log10(abs(hu)) for hu in huMoments.flatten()]


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
    print(momentoImagen)
    media = estadistico[0] 
    var = estadistico[1]
    return distancia_euclidiana(momentoImagen, media, var)


def clasificar(imagen, umbral):

    for i in range(len(estadisticos)):
        analisis = analizarDigito(imagen, estadisticos[i])
        if analisis < umbral:
            return modelos[i]
    return "Photo not recognized"
    

modelos = ["Bus", "Car", "Motorbike", "Three Wheel", "Truck", "Van"]
cargarEstadisticas("estadistico")
imagen = cv.imread("8247421385_9297379bf8_w.jpg", cv.IMREAD_GRAYSCALE)
print(clasificar(imagen, 50))
