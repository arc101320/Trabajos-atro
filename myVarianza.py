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

def varianza(lista):
    """
    Funcion retorna la varianza de un conjunto de datos
    
    input: Lista de datos(no necesariamente ordenados)
    
    output: float, retorna la varianza de los datos
    """
    prom = (1/len(lista)) * sum(lista)
    suma_dif = 0 
    for valor in lista:
        suma_dif += (valor - prom) ** 2  
    
    var = suma_dif / len(lista)
    return var
