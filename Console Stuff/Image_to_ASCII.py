from PIL import Image
import os

os.system('')
grid = ""

im = Image.open(r'image path')
size = im.size
scale = 15
ratio = round(size[0]/size[1])
im = im.resize(((size[0]//scale)*ratio,size[1]//scale))
size = im.size
pix = im.load()
for y in range(size[1]):
    temp = ''
    for x in range(size[0]):
        rgb = (pix[x,y])
        red, green, blue = rgb[0], rgb[1], rgb[2]
        if red == 255 and green == 255 and blue == 255: 
            temp += (f'\x1b[38;2;{0};{0};{0}m█')
        else:
            temp += (f'\x1b[38;2;{red};{green};{blue}m█')
    grid += temp+'\n'

print(grid)

#it has some issues, will be fixed and upgraded!
