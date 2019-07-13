import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
from PIL import Image
import cv2
import os

   
def display_images(directory, numOfImages = 5):
    file_list = glob.glob(directory + "/*/*")
    indicies = random.sample(range(len(file_list)), numOfImages * numOfImages)    
    fig, axes = plt.subplots(nrows=numOfImages,ncols=numOfImages, figsize=(15,15), sharex=True, sharey=True, frameon=False)
    for i,ax in enumerate(axes.flat):
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        #Pick a random picture from the file list
        imgplot = mpimg.imread(file_list[indicies[i]], 0)
        ax.imshow(imgplot)
        ax.text(10,20,file_list[indicies[i]].split("/")[-2], fontdict={"backgroundcolor": "black","color": "white" })
        ax.axis('off')
    plt.tight_layout(h_pad=0, w_pad=0)
    

def resize_image(file, size=299):
    img = Image.open(file)
    img = img.resize((size,size))
    img.save(file)

def check_image(file):
    if not file.endswith(".jpg"):
        #Not ending in .jpg
        print("Deleting (.mat): " + file)
        os.remove(os.path.join(os.getcwd(), file))
    else: 
        flags = cv2.IMREAD_COLOR
        im = cv2.imread(file, flags)
        
        if im is None:
            #Can't read in image
            print("Deleting (None): " + file)
            os.remove(os.path.join(os.getcwd(), file))
        elif len(im.shape) != 3:
            #Wrong amount of channels
            print("Deleting (len != 3): " + file)
            os.remove(os.path.join(os.getcwd(), file))
        elif im.shape[2] != 3:
            #Wrong amount of channels
            print("Deleting (shape[2] != 3): " + file)
            os.remove(os.path.join(os.getcwd(), file))
            
        if os.path.exists(os.path.join(os.getcwd(), file)):
            f = open(os.path.join(os.getcwd(), file), 'rb')
            check_chars = f.read()
            if check_chars[-2:] != b'\xff\xd9':
                #Wrong ending metadata for jpg standard
                print('Deleting (xd9): ' + file)
                os.remove(os.path.join(os.getcwd(), file))
            elif check_chars[:4] != b'\xff\xd8\xff\xe0':
                #Wrong Start Marker / JFIF Marker metadata for jpg standard
                print('Deleting (xd8/xe0): ' + file)
                os.remove(os.path.join(os.getcwd(), file))
            elif check_chars[6:10] != b'JFIF':
                #Wrong Identifier metadata for jpg standard
                print('Deleting (xd8/xe0): ' + file)
                os.remove(os.path.join(os.getcwd(), file))
            elif "beagle_116.jpg" in file or "chihuahua_121.jpg" in file:
                #Using EXIF Data to determine this
                print('Deleting (corrupt jpeg data): ', file)
                os.remove(os.path.join(os.getcwd(), file))  
