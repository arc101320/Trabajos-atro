def moda(lista):
    """
    Función que retorna la moda de cierta cantidad de datos.
    
    :param lista: Lista de datos.
    
    :return: Retorna la moda como un valor (no como un str).
    """
    frecuencias = {}  # Diccionario para almacenar las frecuencias de los valores
    moda = None  # Valor de moda inicialmente desconocido
    max_frecuencia = 0  # Inicializamos la frecuencia máxima en 0

    for valor in lista:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1

        if frecuencias[valor] > max_frecuencia:
            moda = valor
            max_frecuencia = frecuencias[valor]

    return moda
