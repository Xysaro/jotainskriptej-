import os
import re
import sys
import shutil


r, w = os.pipe()

count=0
Current_dir = os.getcwd()

targetfolder= sys.argv[1]

basefolder= os.path.basename(os.path.normpath(targetfolder))
print(basefolder)

moveselect1=Current_dir + "/"+ basefolder+ "/combined"
moveselect2= targetfolder+"combined"
movedir= moveselect2

movedir
print(movedir)

#exit()
movedir= moveselect2
isdir= os.path.isdir(movedir)
print(isdir)
if isdir is False:
    try:

        os.makedirs(movedir)
    except OSError as error:
        print ("Creation of the directory /Combined failed" )
        print(error)

        movedir=moveselect1
        isdir= os.path.isdir(movedir)
        if isdir is False:
            try:
                os.makedirs(movedir)
            except OSError as error:
                print("Failed to create Directory ")
                print (error)
                exit()
        else:
            print("Destination folder already exist")
    else:
        print ("Successfully created the directory ",movedir )

with os.scandir(targetfolder) as it:

    for entry in it:
        #filename=os.path.basename(os.path.normpath(entry.path))
        try:
            with os.scandir(entry.path) as it:
                for entry in it:
                    if re.match("^.*\.(jpg|JPG|gif|GIF|jpg|JPG|png|PNG|jpeg|JPEG|bmp|BMP)$", entry.name) is not None:

                        split = os.path.splitext(entry.name)
                        extension=split[1]
                        nameforfile = os.path.split(os.path.dirname(entry.path)) ## get name of the folder and use it as a name


                        filename = nameforfile[1]+extension
                        origdir= entry.path
                        #print(filename)
                        destination=movedir+"/"+filename
                        print(destination)
                        shutil.copy2(entry.path, destination)
                        count+=1
        except OSError as error:
            print("pieleenmeni",count)
            print(error)
            exit()

        else:
            print("se toimi",count)

print("files:", count)
print("Moved files to ", movedir)
