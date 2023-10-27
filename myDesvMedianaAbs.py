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

def mad(lista):
    
    """
    Funcion retorna la desviacion mediana absoluta de un conjunto de datos
    
    input: Lista de datos(no necesariamente ordenados)
    
    output: float, retorna la desviacion mediana absoluta de los datos
    
    """
    ordenada=sorted(lista)
    n = len(ordenada)
    
    if (n % 2) == 0:
        mediana = (ordenada[n//2] + ordenada[(n//2)+1])/2
    else:
        mediana = ordenada[n+1]/2
    
    
    mad = sum(abs(valor - mediana) for valor in lista)\
    /len(lista)
    return mad
