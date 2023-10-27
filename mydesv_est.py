def d_estandar(lista):
    """
    Funcion retorna la desviacion estandar de un conjunto de datos
    input: Lista de datos(No necesariamente ordenados)
                          
    como la desviacion estandar es la raiz cuadrada de la varianza, 
    se utiliza la funcion varianza() para calcularlo
                                      
    output: retorna la desviacion estandar del conjunto de da
    """
    prom = (1/len(lista)) * sum(lista)
    suma_dif = 0 
    for valor in lista:
        suma_dif += (valor - prom) ** 2  
    
    varianza = suma_dif / len(lista)
    desv=(varianza)**(1/2)
    return desv
