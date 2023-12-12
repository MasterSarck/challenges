# Reto #7
# CONTANDO PALABRAS
# Dificultad: MEDIA

# Enunciado: Crea un programa que cuente cuantas veces se repite cada 
# palabra y que muestre el recuento final de todas ellas.

# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo 
#   resuelvan automáticamente.

parrafo = "Nahue estubo chambeando bajo del sol, luego Nahue se estubo descargando el OSU bajo el sol"

diccionario = {}

for palabra in parrafo.split():
    if palabra not in diccionario.keys():
        diccionario[palabra] = 1 
    else:
        diccionario[palabra] += 1
    
print(diccionario)
