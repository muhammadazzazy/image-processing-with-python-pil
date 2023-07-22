# Import PIL
from PIL import Image, ImageOps

# create image
im1 = Image.open("/home/cat/dog.webp")

# flip vertically
im2 = ImageOps.flip(im1)

# flip horizontally
im2 = ImageOps.mirror(im1)

# turn image into gray scale
im2 = ImageOps.grayscale(im1)

# invert image
im2 = ImageOps.invert(im1)

im2.show()

 
