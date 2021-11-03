from PIL import Image, ImageFilter

filename = "123.png"


with Image.open(filename) as image:
    image = image.filter(ImageFilter.GaussianBlur(radius=20))
    image.save("456.png", "png")




