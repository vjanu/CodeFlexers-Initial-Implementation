import cv2
from PIL import Image
import numpy as np

def colorChange(originalPath):
    name = originalPath[8:-4]
    print(name)
    imagePath="tes-img/"+name+"sharpened_morecontrast.jpg"
    try:
        im = Image.open(imagePath)
    except:
        print("Exception occured in ColorChange.py")    
    im = im.convert('RGBA')
    #To highlight important areas with red in the image
    data = np.array(im)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    # Replace white with red... (leaves alpha values alone...)
    # white_areas = (red >= 80) & (blue >= 80) & (green >= 80)
    black_areas = (red <= 77)  & (green <= 77) & (blue <= 77)
    data[..., :-1][black_areas.T] = (255, 0, 0)
    im3 = Image.fromarray(data)
    #im3.show()
    im3.save("tes-img/"+name+"changedclr1.bmp")

    #To eliminate unimportant areas in the image
    data = np.array(im3)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    white_areas = (red >= 128)  & (green >= 77) & (blue >= 0)
    data[..., :-1][white_areas.T] = (255, 255, 255) # Transpose back needed
    im2 = Image.fromarray(data)
    #im2.show()
    im2.save("tes-img/"+name+"changedclr.bmp")

#######################################################################
    # img = cv2.imread(originalPath)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # im2 = cv2.bitwise_not(img)
    # cv2.imwrite("tes-img/negative.png", im2)
    # print("------ Color Change:Successful -------")
##########################################################################