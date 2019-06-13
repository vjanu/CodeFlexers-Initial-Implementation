import cv2
import numpy as np
import pytesseract
import imutils
from PIL import Image
from pytesseract import image_to_string

# Path of working folder on Disk
src_path = "tes-img/"

def get_stringNewIdCard(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    #comment this and run if uncommenting this fails to read the text
    #img = imutils.resize(img,1024,665)
    
    h0,w0 = img.shape[:2]
    h1 = int(h0/3)
    h2 = int(h0/5)
    w1 = int(w0/3)
    #img = img[h2:h1,w1:w0]
    # img = img[100:700,100:800]
    # cv2.imshow('image0',img)
    # cv2.waitKey(0)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    
    #min filter
    img = cv2.erode(img, kernel, iterations=1)
    
    #max filter
    img = cv2.dilate(img, kernel, iterations=1)
   

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    #result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
    #result = pytesseract.image_to_string(Image.open(src_path + "thres.png"),config="-c tessedit_char_whitelist=01234567890 -psm 6")
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"),config="-c tessedit_char_whitelist=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 6")

    # Remove template file
    # os.remove(temp)
    #print(result)
    brokenlines = result.split('\n');
    print(brokenlines)
    nic = "Not Found"
    for i in brokenlines:
        brokenlinesSep = i.split(" ");
        for j in brokenlinesSep:
            if(len(j) == 12):
            
                print(j)
                nic = j
    
    resultString = "NIC [NEW] :" + nic
    print(resultString)
    return list(nic)
    
    print("---------------------------------------")
   # print(result.split(" "))
    #resultArray = result.split('\n')[0]
    #filterNIC = resultArray.split(" ")
   # nic = "Not Found"
    #for x in filterNIC:
    #    if(len(x) == 12):
     #       nic = x
    #resultString = "NIC [NEW] :" + nic
    #print(resultString)
    #return list(nic)

print('--- Start recognize text from NIC ---')
print(get_stringNewIdCard(src_path + "id10.jpg") )
print(get_stringNewIdCard(src_path + "changedclr.bmp") )
print(get_stringNewIdCard(src_path + "changedclr1.bmp") )
print("------ Done -------")
