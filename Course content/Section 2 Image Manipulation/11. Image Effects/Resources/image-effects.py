from PIL import Image, ImageFilter

# load image
image = Image.open("/home/cat/cat3.png")

# apply effect
blurImage = image.filter(ImageFilter.GaussianBlur(3))
#blurImage = image.filter(ImageFilter.EDGE_ENHANCE)
#blurImage = image.filter(ImageFilter.EMBOSS)
#blurImage = image.filter(ImageFilter.CONTOUR)
#blurImage = image.filter(ImageFilter.SHARPEN)
blurImage.show()


# display image
image.show()
