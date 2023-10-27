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

# +

def read_with_no_header(nombre_archivo, corte):
    """
    abre un archivo y automaticamente elimina la primera fila
    
    input:el nombre de un archivo (debe ser entre comillas)
         corte: el numero desde el cual cortar el titulo
    
    output: list()
    
    """
    
    # Abre el archivo en modo lectura y asegúrate de cerrarlo después
    archivo = open(nombre_archivo,"r")
    lineas = archivo.readlines()
    archivo.close()

    # Verifica si el archivo tiene al menos dos líneas (encabezado y datos)
    if len(lineas) >= 2:
        # Elimina el encabezado
        lineas_sin_encabezado = lineas[corte:]
    else:
        lineas_sin_encabezado = lineas
    return lineas_sin_encabezado

def una_columna(lineas, numero, tipo=float, separador=None):
    """
    Función que crea una lista con el número de la columna elegida.
    
    :param lineas: Conjunto de datos de más de una columna con posibles encabezados.
    :param numero: Número de la columna que se desea elegir.
    :param tipo: Tipo de datos, predeterminado a float.
    :param separador: Separador personalizado, predeterminado a None.
    

    :return: Lista con la columna seleccionada.
    """
    
    columna = []
    

    if separador is None:
        # Intenta detectar el separador en la primera línea que contiene datos
        for linea in lineas:
            elementos = linea.strip().split()
            if len(elementos) > 1:
                for s in [' ', '\t', ',', ';', '|']:
                    if s in elementos[1]:
                        separador = s
                        break
            if separador:
                break

    for linea in lineas:
        elementos = linea.strip().split(separador)
        if len(elementos) > numero:
            valor_columna = elementos[numero]
            
        columna.append(tipo(valor_columna))
    return columna






# -


