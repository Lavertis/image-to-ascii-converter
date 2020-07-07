from PIL import Image
from character_map import *

im = Image.open('images/photo.jpg')
pix = im.load()
pixMap_size = im.size
print(pixMap_size)

file = open("output.txt", "w")
for y in range(pixMap_size[1]):
    for x in range(pixMap_size[0]):
        rgb_sum = pix[x, y][0] + pix[x, y][1] + pix[x, y][2]
        file.write(character(rgb_sum))
    file.write('\n')

file.close()
