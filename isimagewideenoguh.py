import os
import re
import sys
import shutil
from PIL import Image
Current_dir = os.getcwd()
count=0
Landscape=0
Vertical=0
kynnys=3840

targetfolder= sys.argv[1]
print(targetfolder)

basefolder= os.path.basename(os.path.normpath(targetfolder))
print(basefolder)
movedir=Current_dir + "/"+ basefolder

try:

    os.makedirs(movedir+ "/"+ "/Landscape")
except OSError:
    print ("Creation of the directory /Landscape failed or directory already exists" )
else:
    print ("Successfully created the directory /Landscape" )

try:
    os.makedirs(movedir + "/Vertical")

except OSError:
    print ("Creation of the directory /Vertical failed or directory already exists" )
else:
    print ("Successfully created the directory /Vertical" )

with os.scandir(targetfolder) as it:
    for entry in it:

        if re.match("^.*\.(jpg|JPG|gif|GIF|jpg|JPG|png|PNG|jpeg|JPEG|bmp|BMP)$", entry.name) is not None:
            with Image.open(entry.path) as img:
                width, height = img.size

            if width>=kynnys :
                Landscape += 1
                destination = movedir + "/Landscape/" + entry.name
                #os.rename(entry.path , destination)
                shutil.copy2(entry.path, destination)
                print("Destination:",destination)
            elif height>=kynnys :
                Vertical +=1
                destination = movedir + "/Vertical/" + entry.name
                #os.rename(entry.path , destination)
                shutil.copy2(entry.path, destination)
                print("Destination:",destination)
            count += 1

## Show amount of processed images
print ("Images processed",count)
print ("Vertical images:",Vertical)
print ("Landscape images:", Landscape)
