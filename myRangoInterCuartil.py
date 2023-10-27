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

def inter_rango(lista):

    """
    Funcion retorna el rango intercuartil de un conjunto de datos
    
    input: Lista de datos(no necesariamente ordenados)
    
    output: float, retorna el rango intercuartil de los datos
    
    """
    ordenada=sorted(lista)
    n=len(ordenada)
    percentiles=[75,25]
    cuantiles=[]
    for i in percentiles:
        if (n % 2) == 0:
            posicion = (i/100)*n
        else:
            posicion = (i/100)*(n+1)
                                                                                                                                                                                                                                     
        valor_cuantil=ordenada[int(posicion)-1]
        cuantiles.append(valor_cuantil)



    IQR=cuantiles[0]-cuantiles[1]
    return IQR
