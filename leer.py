from PIL import Image
import random

imagen = Image.open("imagen2.png")
anchura = 512
altura = 512
pixeles = imagen.load()

for x in range(0,512):
    color = pixeles[x,0]
    rojo = color[0]
    verde = color[1]
    azul = color[2]
    print(chr(rojo))
    print(chr(verde))
    print(chr(azul))






