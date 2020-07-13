from PIL import Image


import os
from os.path import expanduser
dir = expanduser("~") + '/object_detection/images'
fileList = []
for filename in os.listdir(dir):
    if filename.find('png') != -1:
        fileList.append(filename)
        img = Image.open(dir + '/' + filename) #.resize((400,400)) # (x,y) pixels
        img.convert("RGB").save(dir + '/' + filename.replace('.png', '.jpg'))
print(fileList)



#img = Image.open('images/test/file100.png') #.resize((400,400)) # (x,y) pixels
#img.convert("RGB").save('images/test/file100.jpg')