import numpy as np

def calcular_estadisticas(archivo_entrada, archivo_salida):
    data = []

    # Leer el archivo de entrada
    with open(archivo_entrada, 'r') as file:
        for line in file:
            numbers = [float(num) for num in line.split()]
            data.append(numbers)
    
    # Convertir a un array de NumPy para facilitar los cálculos
    data = np.array(data)
    
    # Calcular medias y varianzas
    medias = np.mean(data, axis=0)
    varianzas = np.var(data, axis=0)

    # Escribir resultados en el archivo de salida
    with open(archivo_salida, 'w') as f:
        f.write(' '.join(map(str, medias)) + '\n')
        f.write(' '.join(map(str, varianzas)) + '\n')
    
    print(f"Modelo estadístico con media y varianza calculadas en {archivo_salida}")

archivo_entrada = "truck" + "Model.txt"
archivo_salida = "truck" + "ModelEstadistico.txt"
calcular_estadisticas(archivo_entrada, archivo_salida)
