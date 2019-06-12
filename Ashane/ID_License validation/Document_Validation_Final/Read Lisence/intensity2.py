from PIL import Image
from PIL import ImageEnhance
#import lisencd-sl-ocr as li

#sourcePath='tes-img/A.jpg'
#sourcePath=""
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
    
    #adjust_contrast('tes-img/6.jpg','tes-img/caterpillar_more_contrast.jpg',0.7)
    #adjust_brightness('tes-img/caterpillar_more_contrast.jpg','tes-img/lighthouse_darkened.jpg', 2.0)
    #adjust_sharpness('tes-img/lighthouse_darkened.jpg','tes-img/mantis_sharpened.jpg', 10.7)
def intensityMain(sourcePath):
    print("------ intensityMain:Started -------")
    #global sourcePath
    #sourcePath=filename
    try:
        adjust_sharpness(sourcePath,'tes-img/sharpened.jpg', 5.7)
        adjust_contrast('tes-img/sharpened.jpg','tes-img/sharpened_morecontrast.jpg',1.7)                    
    except:
        print("Exception occured in intensity")
    
    
    