from PIL import Image
from character_map import *


def get_pixmap(path):
    im = Image.open(path)
    if im.size[0] > 200 and im.size[0] > 200:
        height_to_width_ratio = im.size[1] / im.size[0]
        pixels = 200
        resized_image = im.resize((pixels, int(pixels * height_to_width_ratio)))
        pixmap = resized_image.load()
        pixmap_size = resized_image.size
    else:
        pixmap = im.load()
        pixmap_size = im.size
    print('Original: ' + str(im.size))
    print('Resized: ' + str(pixmap_size))
    return pixmap, pixmap_size


def create_output_file():
    pixmap, pixmap_size = get_pixmap('images/photo.jpg')
    file = open('output.txt', 'w')
    for y in range(pixmap_size[1]):
        for x in range(pixmap_size[0]):
            rgb_sum = pixmap[x, y][0] + pixmap[x, y][1] + pixmap[x, y][2]
            file.write(character(rgb_sum))
        file.write('\n')

    file.close()
