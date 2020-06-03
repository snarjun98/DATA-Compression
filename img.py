import PIL
from PIL import Image


def compress_img(old_img, new_img, mywidth):
    img = Image.open(old_img)
    wpercent = (mywidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
    img.save(new_img)
