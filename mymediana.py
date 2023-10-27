# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

def mediana(lista):
    """
    Funcion mediana retorna la mediana de un conjunto de datos
    
    input: Lista de datos(no necesariamente ordenados)
    
    output: float de la mediana de los datos
    """
    
    ordenada=sorted(lista)
    n = len(ordenada)
    
    if (n % 2) == 0:
        mediana = (ordenada[n//2 +1] + ordenada[n//2])/2
    else:
        mediana = ordenada[n//2]
    return mediana
