from PIL import Image


def get_pixmap():
    im = Image.open('images/photo.jpg')
    print(im.size)
    if im.size[0] > 200 and im.size[0] > 200:
        height_to_width_ratio = im.size[1] / im.size[0]
        pixels = 200
        resized_image = im.resize((pixels, int(pixels * height_to_width_ratio)))
        pixmap = resized_image.load()
        pixmap_size = resized_image.size
    else:
        pixmap = im.load()
        pixmap_size = im.size
    return pixmap, pixmap_size
