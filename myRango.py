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

def rango(lista):
    """
    Funcion rango retorna el rango de un conjunto de datos
    
    input: Lista de datos(no necesariamente ordenados)
    
    output: float, retorna el rango de los datos
    
    
    """
    rango_calculado=max(lista)-min(lista)
    return rango_calculado
