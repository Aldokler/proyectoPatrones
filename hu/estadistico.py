import numpy as np

def calcular_estadisticas(archivo_entrada, archivo_salida):
    data = []

    # Leer el archivo de entrada
    with open(archivo_entrada, 'r') as file:
        for line in file:
            numbers = [float(num) for num in line.split()]
            data.append(numbers)
    medias = np.mean(data, axis=0)
    varianzas = np.var(data, axis=0)
    
    # Normalizar las medias y las varianzas
    mean_medias = np.mean(medias)
    std_dev_medias = np.std(medias)
    normalized_medias = (medias - mean_medias) / std_dev_medias
    
    mean_varianzas = np.mean(varianzas)
    std_dev_varianzas = np.std(varianzas)
    normalized_varianzas = (varianzas - mean_varianzas) / std_dev_varianzas
    
    with open(archivo_salida, 'w') as f:
        f.write(' '.join(map(str, normalized_medias)) + '\n')
        f.write(' '.join(map(str, normalized_varianzas)) + '\n')
    print(f"Modelo estadistico con VAR y MEDIA normalizados en {archivo_salida}")

archivo_entrada = "van" + "Model.txt"
archivo_salida = "van"+"ModelEstadistico.txt"
calcular_estadisticas(archivo_entrada, archivo_salida)
