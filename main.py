import webbrowser
from photo_loading import *
from character_map import *

pixMap, pixMap_size = get_pixmap()
file = open("output.txt", "w")
for y in range(pixMap_size[1]):
    for x in range(pixMap_size[0]):
        rgb_sum = pixMap[x, y][0] + pixMap[x, y][1] + pixMap[x, y][2]
        file.write(character2(rgb_sum))
    file.write('\n')

file.close()
webbrowser.open("output.txt")
