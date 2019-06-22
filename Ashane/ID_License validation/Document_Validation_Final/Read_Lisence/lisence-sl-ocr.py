from flask import jsonify,Flask
import cv2
import numpy as np
import pytesseract
import imutils
from PIL import Image
from pytesseract import image_to_string
import colorChange as cc
import face_detect_lisence as fd
import intensity2 as intensity
import re

# Path of working folder on Disk
src_path = "tes-img/"
filename = ""
# Define as global variable
Expiration = "Not Found"

def get_stringNewLiscence(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
    
    #replace chars with needed characters
    result = result.replace("..", ".")
    result = result.replace("'", "")
    result = result.replace("?", "7")
    result = result.replace('"', "")
    result = result.replace('%', " ")
    result = result.replace('(', " ")
    # Remove template file
    # os.remove(temp)

    resultArray = result.split('\n')
    tempNIC = "Not Found"
    nic = "Not Found"
    lisenceExpiration = "Not Found"
    for x in resultArray:
        #To identify id number
        try:
            if("4d." in x):
                nicContainingLine = x.split("4d.")[1]
                nic = nicContainingLine.split(" ")[0]
                if (len(nic) < 9):
                    nic = nicContainingLine.split(" ")[1]
            elif("d." in x):
                nicContainingLine = x.split("d.")[1]
                nic = nicContainingLine.split(" ")[0]
                if (len(nic) < 9):
                    nic = nicContainingLine.split(" ")[1]
            #To identify expiration dates
            if("4b." in x):
                lisenceExpiration = x.split("4b.")[1]          
            if (len(lisenceExpiration) < 10):
                if("b." in x):
                    x = x.replace(" ", "")
                    lisenceExpiration = x.split("b.")[1]
                elif("40." in x):
                    lisenceExpiration = x.split("40.")[1]
        except:
            print("Exception Occured")
            continue
                
    #When 4d. is not found in image           
    if(nic == "Not Found"):
        nextresult = result.split('\n')
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        #print(nextresult)
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        for z in nextresult:
            nextresult2 = z.split(' ')           
            for y in nextresult2:
                if("V" in y):
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    #print(nextresult2.index(y))
                    listIndex=nextresult2.index(y)
                    tempNIC=nextresult2[listIndex-1]
                    #re.split("[^1-9]*",tempNIC)
                    #tempNIC=int("".join(filter(str.isdigit, tempNIC)))
                    tempNIC = re.sub(r"\D+", "", tempNIC)
                    tempNIC = re.sub(r"\W+", "", tempNIC, flags=re.I)
         
                    splitLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ|"
                    for char in splitLetters:  
                        tempNIC = tempNIC.replace(char,'')  
                    #re.sub("A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z", "", tempNIC)
                    #re.split('A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z', tempNIC)
                    #print("ssssssssssssssssssssssssssssssssssss",tempNIC)
                    if((listIndex > 0) and ((len(tempNIC) == 9) or len(tempNIC) == 12)):
                        nic = tempNIC
                    elif((listIndex == 0) and ((len(tempNIC) == 9) or len(tempNIC) == 12)):
                        nic = tempNIC
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    
                elif("v" in y):
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    #print(nextresult2.index(y))
                    listIndex=nextresult2.index(y)
                    tempNIC=nextresult2[listIndex-1]
                    tempNIC = re.sub(r"\D+", " ", tempNIC)
                    tempNIC = re.sub(r"\W+", " ", tempNIC, flags=re.I)
         
                    splitLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ|"
                    for char in splitLetters:  
                        tempNIC = tempNIC.replace(char,'')  
                    #print("ssssssssssssssssssssssssssssssssssss",tempNIC)
                    if((listIndex > 0) and ((len(tempNIC) == 9) or len(tempNIC) == 12)):
                        nic = tempNIC
                    elif((listIndex == 0) and ((len(tempNIC) == 9) or len(tempNIC) == 12)):
                        nic = tempNIC                    
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            #print(nextresult2)
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    
    nic = nic.replace('.', "")            
    resultArray = [nic,lisenceExpiration]
    
    if(lisenceExpiration != "Not Found"):
        global Expiration
        Expiration=lisenceExpiration
    print(resultArray) 
    if(nic == "Not Found"):
        print("[LISENCE]NIC not found --> Resizing the image")
        nic = get_stringNewLiscenceResized(img_path)
    
    if(len(nic) == 9):
        print("[LISENCE]NIC contains 9 digits only --> Converted to 12 digit format")
        nic = '19' + nic[:5]+'0'+nic[5:]
    #print(result)    
    return list(nic)
    
def get_stringNewLiscenceResized(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    #comment this and run if uncommenting this fails to read the text
    img = imutils.resize(img,4096,665) 

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
    result = result.replace("..", ".")
    result = result.replace("'", "")
    result = result.replace("?", "7")
    result = result.replace('"', "")
    result = result.replace('%', " ")
    result = result.replace('(', " ")
    # Remove template file
    # os.remove(temp)

    resultArray = result.split('\n')
    tempNIC = "Not Found"
    nic = "Not Found"
    lisenceExpiration = "Not Found"
    for x in resultArray:
        #To identify id number
        try:
            if("4d." in x):
                nicContainingLine = x.split("4d.")[1]
                nic = nicContainingLine.split(" ")[0]
                if (len(nic) < 9):
                    nic = nicContainingLine.split(" ")[1]
            elif("d." in x):
                nicContainingLine = x.split("d.")[1]
                nic = nicContainingLine.split(" ")[0]
                if (len(nic) < 9):
                    nic = nicContainingLine.split(" ")[1]
            #To identify expiration dates
            if("4b." in x):
                lisenceExpiration = x.split("4b.")[1]          
            if (len(lisenceExpiration) < 10):
                if("b." in x):
                    x = x.replace(" ", "")
                    lisenceExpiration = x.split("b.")[1]
                elif("40." in x):
                    lisenceExpiration = x.split("40.")[1]
        except:
            print("Exception Occured")
            continue
                
    if(nic == "Not Found"):
        nextresult = result.split('\n')
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        #print(nextresult)
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        for z in nextresult:
            nextresult2 = z.split(' ')
            
            for y in nextresult2:
                if("V" in y):
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    #print(nextresult2.index(y))
                    listIndex=nextresult2.index(y)
                    tempNIC=nextresult2[listIndex-1]
                    #re.split("[^1-9]*",tempNIC)
                    tempNIC = re.sub(r"\D+", "", tempNIC)
                    tempNIC = re.sub(r"\W+", "", tempNIC, flags=re.I)
         
                    splitLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ|"
                    for char in splitLetters:  
                        tempNIC = tempNIC.replace(char,'')   
                    #print("ssssssssssssssssssssssssssssssssssss",tempNIC)
                    if((listIndex > 0) and ((len(tempNIC) == 9) or len(tempNIC) == 12)):
                        nic = tempNIC
                    elif((listIndex == 0) and ((len(tempNIC) == 9) or len(tempNIC) == 12)):
                        nic = tempNIC                   
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    
                elif("v" in y):
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    #print(nextresult2.index(y))
                    listIndex=nextresult2.index(y)
                    tempNIC=nextresult2[listIndex-1]
                    tempNIC = re.sub(r"\D+", "", tempNIC)
                    tempNIC = re.sub(r"\W+", "", tempNIC, flags=re.I)
         
                    splitLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ|"
                    for char in splitLetters:  
                        tempNIC = tempNIC.replace(char,'')   
                    #re.sub("A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z", "", tempNIC)
                    #re.split('A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z', tempNIC)
                    #print("ssssssssssssssssssssssssssssssssssss",tempNIC)
                    if((listIndex > 0) and ((len(tempNIC) == 9) or len(tempNIC) == 12)):
                        nic = tempNIC
                    elif((listIndex == 0) and ((len(tempNIC) == 9) or len(tempNIC) == 12)):
                        nic = tempNIC                    
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            #print(nextresult2)
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    
    nic = nic.replace('.', "")              
    resultArray = [nic,lisenceExpiration]
    if(lisenceExpiration != "Not Found"):
        global Expiration
        Expiration=lisenceExpiration
    if(len(nic) == 9):
        print("[LISENCE]NIC contains 9 digits only --> Converted to 12 digit format")
        nic = '19' + nic[:5]+'0'+nic[5:]
    #print(result)
    print(resultArray)
    return list(nic)

#Main method imlementation as a web service
app = Flask(__name__)    

@app.route("/lisence/<string:location>")
def main(location):
    global filename
    filename = location   
    print('--- Start recognize text from lisence ---')
    try:  
        if(fd.checkFaces(src_path + filename) >= 1): 
            intensity.intensityMain(src_path + filename)
            cc.colorChange(src_path + filename)
            result1 = get_stringNewLiscence(src_path +filename)
            if(result1 == ['1', '9', 'N', 'o', 't', ' ', 'F', '0', 'o', 'u', 'n', 'd'] ):
                result2 = get_stringNewLiscence(src_path + "changedclr1.bmp")
                if(result2 == ['1', '9', 'N', 'o', 't', ' ', 'F', '0', 'o', 'u', 'n', 'd']): 
                    result3 = get_stringNewLiscence(src_path + "changedclr.bmp")
                    print(result3)
                    ExtractedNIC=result3
                    Description="Processed"
                else:
                    print(result2)
                    ExtractedNIC=result2
                    Description="Processed"
            else:
                print(result1)
                ExtractedNIC=result1
                Description="Processed"
        else:
            ExtractedNIC="null"
            Description="Unable to recognize human faces" 
        print("Expiration",Expiration) 
    except:
        print("Exception occured in lisence-sl-ocr.py")
        ExtractedNIC="null"
        Description="Unexpected error,Unable to process the image,Please check the path" 
    print("------ Done -------")
    
    data =[{'ExtractedNIC' : ExtractedNIC ,'Expiration' : Expiration,'Description':Description}]
    
    return jsonify(data), 200
    
    #return as a json object
   # return jsonify(
   # ExtractedNIC = ExtractedNIC,
   # Expiration = Expiration,
   # Description = Description
    #)  
app.run(debug=True,host="0.0.0.0",port=8088)