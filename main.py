import webbrowser

from photo import *

image_path = choose_image_path()
create_output_file(image_path)
webbrowser.open('output.txt')
