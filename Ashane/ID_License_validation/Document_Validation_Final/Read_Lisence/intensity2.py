from PIL import Image
from PIL import ImageEnhance

#To adjust the sharpness of image
def adjust_sharpness(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Sharpness(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)
    
#To adjust the brightness of image                   
def adjust_brightness(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Brightness(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)
    
#To adjust the contrast of image  
def adjust_contrast(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Contrast(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)    
    
def intensityMain(sourcePath):
    name = sourcePath[8:-4]
    print(name)
    print("------ intensityMain:Started -------")
  
    try:
        adjust_sharpness(sourcePath,'tes-img/'+name+'sharpened.jpg', 5.7)
        adjust_contrast('tes-img/'+name+'sharpened.jpg','tes-img/'+name+'sharpened_morecontrast.jpg',1.7)                    
    except:
        print("Exception occured in intensity")
    
    
    