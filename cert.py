from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
def certi(name):
    os.chdir(r'C:\Users\KIIT\Desktop\certificates')
    img = Image.open('PARTICIPATION.png')

    myFont = ImageFont.truetype('Rubik-Regular.ttf', 250)
    I1 = ImageDraw.Draw(img)
    I1.text((1450, 2359), name.center(55), font=myFont, fill=(0, 0, 0))
    # img.show()
    os.chdir(r'C:\Users\KIIT\Desktop\certificates\esports2')
    img.save(name+".png")
    os.chdir(r'C:\Users\KIIT\Desktop\certificates')
