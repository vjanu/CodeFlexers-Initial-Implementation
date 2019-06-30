import cv2
from PIL import Image
import numpy as np

def colorChange(imagepath):
    name = imagepath[8:-4]
    print(name)
    im = Image.open(imagepath)
    im = im.convert('RGBA')

    data = np.array(im)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

    # Replace white with red... (leaves alpha values alone...)
    # white_areas = (red >= 80) & (blue >= 80) & (green >= 80)

    black_areas = (red <= 120) & (blue <= 120) & (green <= 120)
    data[..., :-1][black_areas.T] = (255, 0, 0)
    im3 = Image.fromarray(data)
    # im3.show()
    im3.save("tes-img/"+name+"changedclr1.bmp")

    data = np.array(im3)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

    white_areas = (red >= 100) & (blue >= 69) & (green >= 19)
    data[..., :-1][white_areas.T] = (255, 255, 255) # Transpose back needed

    im2 = Image.fromarray(data)
    # im2.show()
    im2.save("tes-img/"+name+"changedclr.bmp")