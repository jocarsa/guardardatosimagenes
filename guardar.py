from PIL import Image
import random

imagen = Image.open("imagen.png")
anchura = 512
altura = 512
pixeles = imagen.load()

cadena = "Hola que tal como estais"
contador = 0
for caracter in cadena:
    print(ord(caracter))
    pixeles[contador,0] = (ord(caracter),0,0)
    contador += 1

imagen.save("imagen2.png")



