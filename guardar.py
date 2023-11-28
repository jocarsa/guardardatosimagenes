from PIL import Image

imagen = Image.open("imagen.png")

pixeles = imagen.load()

print(pixeles)
