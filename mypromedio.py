def promedio(lista):
    """
    Funcion promedio retorna el promedio aritmetico de un conjunto de datos
                
    input: Lista de datos (no necesariamente ordenados)
                        
    salida: promedio/ media aritmetica, (float)
                                
    """
    promedio = (1/len(lista))*(sum(lista))
    return round(promedio,2)
