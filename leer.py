from PIL import Image
import random

imagen = Image.open("imagen2.png")
anchura = 512
altura = 512
pixeles = imagen.load()


for y in range(0,512):
    for x in range(0,512):

        color = pixeles[x,y]
        rojo = color[0]
        verde = color[1]
        azul = color[2]
        print(chr(rojo), end='')
        print(chr(verde), end='')
        print(chr(azul), end='')






