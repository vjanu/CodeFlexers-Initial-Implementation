import cv2
import sys
import imutils
from PIL import Image

# Path of working folder on Disk
#src_path = "tes-img/"

def checkFaces(img_path):
    # Get user supplied values
    count = 0
    picture= Image.open(img_path)
    imagePath = img_path
    cascPath = "haarcascade_frontalface_default.xml"    

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)

    # To resize the image for better view
    image = imutils.resize(image,512,665)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Found {0} faces!".format(len(faces)))

    if(len(faces)!=1):
        print("Please insert a valid image")
        if(count != 3):
            picture.rotate(90, expand=True).save(img_path)
            checkFaces(img_path)
            count=count+1
    else:
        print("Image verified")

    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # cv2.imshow("Faces found", image)
    # cv2.waitKey(0)
        return len(faces)

