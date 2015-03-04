import sys
import os
import math
from PIL import Image

#example:
#python encode.py filename image.png
#
#+-------->x
#|
#|  pixel[x,y]
#v
#y
#
#There are always noise after screen capture, the value of pixel
#will change around 10 to 20.
#So instead of using r,g,b to express three byte in one pixel,
#one byte is divided into three parts as MSB

with open(sys.argv[1], "rb") as f:
    #get file size to calculate the number of pixels
    size = os.stat(sys.argv[1]).st_size
    pixelNum = int (math.ceil(float(size)))

    #create a new image, there must be Alpha channel included
    length = int(math.sqrt(pixelNum))+5
    im = Image.new("RGBA",(length,length),"black")

    #draw identify boundary
    pixel = im.load()
    for i in range(0,length):
        pixel[0,i]=(255,255,255)
        pixel[i,0]=(255,255,255)
        pixel[length-1,i]=(255,255,255)
        pixel[i,length-1]=(255,255,255)

    #read byte by byte entil the end of file
    #32 is space, 10 in newline
    for i in range(0,pixelNum):
        rawdata = f.read(1)
        if rawdata== "":
           rawdata = 0 #or set to space/newline, TBD
        else:
            rawdata = ord(rawdata)
        #divide one byte into three bytes to remove noise when cap screen
        #0xabcdefgh -> 0xabc00000, 0xdef00000, 0xgh000000
        myList = [rawdata&int('11100000',2),(rawdata<<3)&int('11100000',2),rawdata<<6&(int('11000000',2))]
        #write value into pixel as RGB
        pixel[2+i%(length-4),2+i/(length-4)]=(myList[0],myList[1],myList[2])

    im.save(sys.argv[2],"PNG")
