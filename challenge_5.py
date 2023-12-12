# Reto #5
# ASPECT RATIO DE UNA IMAGEN
# Dificultad: DIFÍCIL

# Enunciado: Crea un programa que se encargue de calcular el aspect 
# ratio de una imagen a partir de una url.
# - Nota: Esta prueba no se puede resolver con el playground 
# online de Kotlin. Se necesitaAndroid Studio.
# - Url de ejemplo: 
# https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
# - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.

import urllib.request
from PIL import Image

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

imagen = Image.open(urllib.request.urlopen(url))
ancho, alto = imagen.size
ratio_de_aspecto = ancho / alto

print(f"Esto es el ratio de aspecto de la imagen: {ratio_de_aspecto}")
