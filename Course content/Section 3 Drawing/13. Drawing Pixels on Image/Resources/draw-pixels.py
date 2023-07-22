from PIL import Image, ImageColor, ImageDraw

# create image
image = Image.new("RGB", (512, 512), ImageColor.getrgb("#ffffff"))

# get image width, height
width, height = image.size

# loop
for x in range(height):
    # draw dots
    image.putpixel((x, x), (0, 0, 0, 255))
    image.putpixel((x, -x), (0, 0, 0, 255))
    image.putpixel((x,100), "blue")

# show image
image.show()

 
