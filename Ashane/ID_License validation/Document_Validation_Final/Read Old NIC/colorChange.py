import cv2
from PIL import Image
import numpy as np

def colorChange(imagepath):
    im = Image.open(imagepath)
    im = im.convert('RGBA')

    data = np.array(im)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    #Replace the RGB values less than 77 to RED
    black_areas = (red <= 77) & (blue <= 77) & (green <= 77)
    data[..., :-1][black_areas.T] = (255, 0, 0)
    im3 = Image.fromarray(data)
    #im3.show()
    im3.save("tes-img/changedclr1.bmp")

    data = np.array(im3)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    #Replace the unwanted pixels to WHITE
    white_areas = (red >= 100) & (blue >= 69) & (green >= 19)
    data[..., :-1][white_areas.T] = (255, 255, 255) # Transpose back needed
    im2 = Image.fromarray(data)
    #im2.show()
    im2.save("tes-img/changedclr.bmp")