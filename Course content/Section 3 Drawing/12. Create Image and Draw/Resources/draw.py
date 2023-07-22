from PIL import Image, ImageColor, ImageDraw

# create image
image = Image.new("RGB", (512, 512), ImageColor.getrgb("#ffffff"))

draw = ImageDraw.Draw(image)

# draw line
draw.line([(0,0), (100,100)], fill="red", width=5)

# draw circle
draw.ellipse((50, 100, 150, 200), fill=(100,64,32), outline=(0, 0, 0))

# draw rectangle
draw.rectangle((200, 100, 300, 200), fill="purple", outline="green")

# display image
image.show()

 
