from PIL import Image
import random

imagen = Image.open("imagen.png")
anchura = 512
altura = 512
pixeles = imagen.load()

cadena = "Hola que tal como estais"
contador = 0
for caracter in cadena:
    print(caracter)



