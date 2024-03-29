from flask import jsonify,Flask
import re
import os
import cv2
import numpy as np
import pytesseract
import imutils
from PIL import Image
from pytesseract import image_to_string
import colorChange as cc
import face_detect_nic as fd

# Path of working folder on Disk
src_path = "tes-img/"
filename = ""
imgname = ""

def get_stringOldIdCard2(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # comment this and run if uncommenting this fails to read the text
    #img = imutils.resize(img,1024,665)
    
    h0,w0 = img.shape[:2]
    h1 = int(h0/3)
    #h1 = int(h0/2)
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
    cv2.imwrite(src_path +imgname+ "removed_noise.png", img)

    # Apply threshold to get image with only black and white
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path +imgname+ "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path +imgname+ "thres.png"),config="-c tessedit_char_whitelist=01234567890IilVv -psm 6")
    
    # Remove template file
    # os.remove(temp)
    
    #result = re.sub(r"[^0-9IilVv]+", "", result)
    result = result.replace("I", "1")
    result = result.replace("i", "1")
    result = result.replace("l", "1")
    # result = result.replace("g", "0")
    print(result)
    resultArray = result.split('\n')
    nic = "Not Found"
    for x in resultArray:
        if(" v" in x):
            nic = x
            nic = nic.split(" v")[0]
            nic = nic.replace(" ", "")
            if(len(nic) == 9 ):
                break
        elif (" V" in x):
            nic = x
            nic = nic.split(" V")[0]
            nic = nic.replace(" ", "")
            if(len(nic) == 9 ):
                break
        elif ("v" in x):
            nic = x
            nic = nic.split("v")[0]
            #nic = re.sub(r"[^0-9]+", "", nic)
            # break
        elif ("V" in x):
            nic = x
            nic = nic.split("V")[0]
            # break
        elif (len(x) == 9):
                nic = x
    
    nic = nic.replace(" ", "")
    nic = nic.replace("v","0")
    nic = nic.replace("]", "1")
    nic = re.sub(r"[^0-9]+", "", nic)
    nic = nic[-9:]
    #print(resultArray)
    if(len(nic) == 9 ):
        print("Old NIC contains 9 digits only --> Converted to 12 digit format")
        nic = '19' + nic[:5]+'0'+nic[5:]
    #resultString = "NIC [OLD] :" + nic
    # print(resultString)
    return nic

def get_stringOldIdCard(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # comment this and run if uncommenting this fails to read the text
    img = imutils.resize(img,1024,665)
    
    h0,w0 = img.shape[:2]
    #h1 = int(h0/3)
    h1 = int(h0/2)
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
    cv2.imwrite(src_path +imgname+ "removed_noise.png", img)

    # Apply threshold to get image with only black and white
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path +imgname+ "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path +imgname+ "thres.png"),config="-c tessedit_char_whitelist=01234567890IilVv -psm 6")
    
    # Remove template file
    # os.remove(temp)
    
    result = re.sub(r"[^0-9IilVv]+", "", result)
    result = result.replace("I", "1")
    result = result.replace("i", "1")
    result = result.replace("l", "1")
    # result = result.replace("g", "0")
    print(result)
    resultArray = result.split('\n')
    nic = "Not Found"
    for x in resultArray:
        if(" v" in x):
            nic = x
            nic = nic.split(" v")[0]
            nic = nic.replace(" ", "")
            if(len(nic) == 9 ):
                break
        elif (" V" in x):
            nic = x
            nic = nic.split(" V")[0]
            nic = nic.replace(" ", "")
            if(len(nic) == 9 ):
                break
        elif ("v" in x):
            nic = x
            nic = nic.split("v")[0]
            #nic = re.sub(r"[^0-9]+", "", nic)
            # break
        elif ("V" in x):
            nic = x
            nic = nic.split("V")[0]
            # break
        elif (len(x) == 9):
                nic = x
    nic = re.sub(r"[^0-9]+", "", nic)
    nic = nic.replace(" ", "")
    nic = nic.replace("v","0")
    nic = nic.replace("]", "1")
    nic = nic[-9:]
    #print(resultArray)
    if(len(nic) == 9 ):
        print("Old NIC contains 9 digits only --> Converted to 12 digit format")
        nic = '19' + nic[:5]+'0'+nic[5:]
    #resultString = "NIC [OLD] :" + nic
    # print(resultString)
    else :
        nic = get_stringOldIdCard2(img_path)
    return list(nic)

#Main method imlementation as a web service
app = Flask(__name__)

@app.route("/nic/<string:location>")
def main(location):
    global filename
    global imgname
    filename = location 
    imgname = location[:-4]
    print(imgname)
    print('--- Start recognize text from NIC ---')
    try: 
        if(fd.checkFaces(src_path + filename) >= 1):  
            cc.colorChange(src_path + filename)  
            ExtractedNIC = get_stringOldIdCard(src_path +imgname+ "changedclr1.bmp")
            print(ExtractedNIC)
            if(len(get_stringOldIdCard(src_path + imgname+"changedclr1.bmp"))!=12):
                ExtractedNIC = get_stringOldIdCard(src_path +imgname+ "changedclr.bmp") 
                print(ExtractedNIC)  
            Description="Processed"
        else:
            ExtractedNIC="null"
            Description="Unable to recognize human faces" 
    except Exception as e:
        print(e)
        ExtractedNIC="null"
        Description="Unexpected error,Unable to process the image,Please check the path" 
    print("------ Done -------")
    
    os.remove(src_path +imgname+ "changedclr1.bmp")
    os.remove(src_path +imgname+ "changedclr.bmp")
    os.remove(src_path +imgname+ "removed_noise.png")
    os.remove(src_path +imgname+ "thres.png")

    data =[{'ExtractedNIC' : ExtractedNIC ,'Description':Description}]
    
    return jsonify(data), 200  
        
app.run(debug=False,host="0.0.0.0",port=8089)
