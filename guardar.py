from PIL import Image
import random

imagen = Image.open("imagen.png")
anchura = 512
altura = 512
pixeles = imagen.load()
for x in range(0,anchura):
    for y in range(0,altura):
        rojo = random.randint(0,255)
        verde = random.randint(0,255)
        azul = random.randint(0,255)
        pixeles[x,y] = (rojo,verde,azul)

imagen.save("imagen2.png")
