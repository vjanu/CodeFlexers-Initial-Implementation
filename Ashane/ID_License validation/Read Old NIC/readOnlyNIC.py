import cv2
import numpy as np
import pytesseract
import imutils
from PIL import Image
from pytesseract import image_to_string
import colorChange
import face_detect_nic as fd

# Path of working folder on Disk
src_path = "tes-img/"

def get_stringOldIdCard(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # comment this and run if uncommenting this fails to read the text
    img = imutils.resize(img,1024,665)
    
    h0,w0 = img.shape[:2]
    h1 = int(h0/3)
    h2 = int(h0/5)
    w2 = int(w0/5)
    w1 = int(w0/5)*4
    img = img[h2:h1,w2:w1]

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    # Apply threshold to get image with only black and white
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"),config="-c tessedit_char_whitelist=01234567890IilVv -psm 6")
    
    # Remove template file
    # os.remove(temp)
    
    result = result.replace("I", "1")
    result = result.replace("i", "1")
    result = result.replace("l", "1")
    # result = result.replace("g", "0")
    
    resultArray = result.split('\n')
    nic = "Not Found"
    for x in resultArray:
        if(" v" in x):
            nic = x
            nic = nic.split(" v")[0]
            nic = nic.replace(" ", "")
            if(len(nic) >= 9 ):
                break
        elif (" V" in x):
            nic = x
            nic = nic.split(" V")[0]
            nic = nic.replace(" ", "")
            if(len(nic) >= 9 ):
                break
        elif ("v" in x):
            nic = x
            nic = nic.split("v")[0]
            # break
        elif ("V" in x):
            nic = x
            nic = nic.split("V")[0]
            # break
    nic = nic.replace(" ", "")
    nic = nic.replace("v","0")
    nic = nic[-9:]
    #print(resultArray)
    if(len(nic) == 9 ):
        print("Old NIC contains 9 digits only --> Converted to 12 digit format")
        nic = '19' + nic[:5]+'0'+nic[5:]
    #resultString = "NIC [OLD] :" + nic
    # print(resultString)
    return list(nic)


#print(fd.noOfFaces)
if(fd.noOfFaces == 1):
    print('--- Start recognize text from NIC ---')
# print(get_stringOldIdCard(src_path + "changedclr.bmp") )
# if(get_stringOldIdCard(src_path + "changedclr.bmp")==['N', 'o', 't', 'F', 'o', 'u', 'n', 'd']):
#     #name of the original file:CHANGE THIS ACCORDINGLY
#     print(get_stringOldIdCard(src_path + "n.jpg") )


    print(get_stringOldIdCard(src_path + "changedclr1.bmp") )
    if(len(get_stringOldIdCard(src_path + "changedclr1.bmp"))!=12):
        print(get_stringOldIdCard(src_path + "changedclr.bmp") )    
    print("------ Done -------")
