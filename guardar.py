from PIL import Image

imagen = Image.open("imagen.png")

pixeles = imagen.load()

pixeles[0,0] = (255,0,0)

imagen.save("imagen2.png")
