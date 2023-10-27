def cuantil(lista,numero,valor=False):
    """
    Funcion determina los cuantiles de una lista
    ----
    lista: lista de datos para ser procesados
    numero: numero del 1-100 para determinar 
    el percentil de la lista de datos
    valor: predeterminado false para que no retorne el valor del cuantil, 
    si es True retorna 
    ----
    input: Lista de datos(No necesariamente ordenados) , numero del percentil por el cual evaluar
    valor, si determinar el valor o posicion (predeterminado para solo posicion)  
                                                                         
    output: valor = False: retorna posicion del cuantil en la lista
    valor = True: retorna valor del cuantil buscado
                                                                                             
    """
    ordenada=sorted(lista)
    n=len(ordenada)
    # para determinar la posicion
    if not valor:
        if (n % 2) == 0:
            cuantil = (numero/100)*n
        else:
            cuantil = (numero/100)*(n+1)
        return cuantil
                                                                                                                                                                             
                                                                                                                                                                             
    else:
        if (n % 2) == 0:
            cuantil = (numero/100)*n
        else:
            cuantil = (numero/100)*(n+1)
                                                                                                                                                                                                                                     
        valor_cuantil=ordenada[int(cuantil)-1]
        return valor_cuantil
