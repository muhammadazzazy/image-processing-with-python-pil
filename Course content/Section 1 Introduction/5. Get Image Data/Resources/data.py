# Import module
from PIL import Image

# Load image from disk (change the path)
im = Image.open("/home/cat/cat.png")

# Get format
print(image.format)

# Get color mode
print(image.mode)

# Get size, tuple
print(image.size)

# Get width in pixels
print(image.width)

# Get height in pixels
print(image.height)

# Get more information
print(image.info)

# Show image
im.show()
