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
import face_detect_enic as fd
import time

# Path of working folder on Disk
src_path = "tes-img/"
filename = ""
imgname = ""

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
    # mask size affects to remove noise
    kernel = np.ones((3, 3), np.uint8)
    
    #max filter
    img = cv2.dilate(img, kernel, iterations=1)
   
    #min filter
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path +imgname+ "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    blur = cv2.GaussianBlur(img, (1, 1), 0)
    ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path +imgname+ "thres.png", img)

    # Recognize text with tesseract for python
    #result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
    #result = pytesseract.image_to_string(Image.open(src_path + "thres.png"),config="-c tessedit_char_whitelist=01234567890 -psm 6")
    result = pytesseract.image_to_string(Image.open(src_path +imgname+ "thres.png"),config="-c tessedit_char_whitelist=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 6")

    # Remove template file
    # os.remove(temp)
    #print(result)
    result = re.sub(r"[^0-9]+", " ", result)
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

#Main method imlementation as a web service
app = Flask(__name__)
@app.route("/enic/<string:location>")
def main(location):
    global filename
    global imgname
    filename = location 
    imgname = location[:-4]
    print(imgname)
    print('--- Start recognize text from eNIC ---')
    try: 
        print(fd.checkFaces(src_path + filename))
        if(int(fd.checkFaces(src_path + filename)) >= 1):
            cc.colorChange(src_path + filename)
            # print(len(get_stringNewIdCard(src_path +filename)) )
            ExtractedNIC = get_stringNewIdCard(src_path + filename)
            if(len(ExtractedNIC) != 12):
                # print(get_stringNewIdCard(src_path + "changedclr1.bmp") )
                ExtractedNIC = get_stringNewIdCard(src_path +imgname+ "changedclr1.bmp")            
                if(len(ExtractedNIC) != 12):
                    # print(get_stringNewIdCard(src_path + "changedclr.bmp") ) 
                    ExtractedNIC = get_stringNewIdCard(src_path +imgname+ "changedclr.bmp")
            Description = "Processed"
              #remove created images
            #TODO:REMOVE SOURSE FILE ALSO
            os.remove(src_path +imgname+ "changedclr1.bmp")
            os.remove(src_path +imgname+ "changedclr.bmp")
            os.remove(src_path +imgname+ "removed_noise.png")
            os.remove(src_path +imgname+ "thres.png")
        else:
            ExtractedNIC = "null"
            Description = "Unable to recognize human faces" 
    except Exception as e:
        print(e)
        ExtractedNIC = "null"
        Description = "Unexpected error,Unable to process the image,Please check the path" 
    print("------ Done -------")

    data =[{'ExtractedNIC' : ExtractedNIC ,'Description':Description}]
    
    return jsonify(data), 200 
        
app.run(debug=False,host="0.0.0.0",port=8087)