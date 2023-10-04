def moda ()
"""
moda: str
  la moda de la muestra (categoria/etiqueta)
"""
#Encontrar el conjunto de elementos unicos
categorias=[]
for v in a:
    if v not in categorias:
        categorias.append(v)

cuentas=[]
for c in categorias:
    n=0
    for val in a:
        n +=1
    cuentas.append(n)
i = max(cuentas)
moda = cuentas [i]
return moda
