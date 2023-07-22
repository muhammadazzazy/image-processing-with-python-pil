# Load PIL
from PIL import Image, ImageFont, ImageDraw  
      
# Load image and create image object  
image = Image.open('/home/cat/cat.png')  

# Draw object on image
draw = ImageDraw.Draw(image)  

# Load font (Check Path on your computer)
font = ImageFont.truetype(r'/usr/share/fonts/truetype/fonts-deva-extra/samanata.ttf', 20)  

# Text to write on image
text = 'NO LAUGH \n NO LIFE'
  
# Add text to image
draw.text((5, 5), text, font = font, align ="left")  

# Show image
image.show()  
