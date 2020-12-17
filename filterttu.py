import os
import re
from PIL import Image
Current_dir = os.getcwd()
count=0
Landscape=0
Vertical=0

try:

    os.mkdir(Current_dir + "/Landscape")
except OSError:
    print ("Creation of the directory /Landscape failed or directory already exists" )
else:
    print ("Successfully created the directory /Landscape" )
    
try:
    os.mkdir(Current_dir + "/Vertical")
   
except OSError:
    print ("Creation of the directory /Vertical failed or directory already exists" )
else:
    print ("Successfully created the directory /Vertical" )

with os.scandir(Current_dir) as it:
    for entry in it:
        
        if re.match("^.*\.(jpg|JPG|gif|GIF|jpg|JPG|png|PNG|jpeg|JPEG|bmp|BMP)$", entry.name) is not None:
            with Image.open(entry.path) as img:
                width, height = img.size

            print("Image:",entry)
            suhde= int(width/height)
            print(suhde)
            if suhde >= 1 :
                Landscape += 1
                destination = Current_dir + "/Landscape/" + entry.name
                os.rename(entry.path , destination)
                print("Destination:",destination)
            if suhde == 0 :
                Vertical +=1
                destination = Current_dir + "/Vertical/" + entry.name
                os.rename(entry.path , destination)
                print("Destination:",destination)
            count += 1

## Show amount of processed images
print ("Images processed",count)
print ("Vertical images:",Vertical)
print ("Landscape images:", Landscape)

