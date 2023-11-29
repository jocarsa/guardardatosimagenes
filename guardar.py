from PIL import Image
import random

imagen = Image.open("imagen.png")
anchura = 512
altura = 512
pixeles = imagen.load()

archivo = open("instrucciones.txt",'r', encoding='utf-8')

cadena = archivo.read()

contador = 0
fila = 0

for i in range(0,len(cadena),3):
    try:
        rojo = ord(cadena[i])
        verde = ord(cadena[i+1])
        azul = ord(cadena[i+2])
        pixeles[contador,fila] = (rojo,verde,azul)
        pass
    except:
        pass
    contador += 1
    if contador == 511:
        contador = 0
        fila += 1

imagen.save("imagen2.png")
archivo.close()



