import sys
import os
import math
from PIL import Image

#example:
#python decode.py image.png filename
#+-------->x
#|
#|  image
#v
#y

#return the length and second identity point
def findlength(width,height):
    length = 0
    flag = 0
    for y in range(0,height-1):
            for x in range(0,width):
                #remove Alpha channel if necessary
                if (pixel[x,y][0:3] == (255,255,255) and pixel[x,y+1][0:3] == (0,0,0)):
                    length += 1
                elif (pixel[x,y][0:3] == (255,255,255) and pixel[x,y+1][0:3] == (255,255,255)):
                    flag += 1
                    if (flag == 2):
                        return length-2,x,y


with open(sys.argv[2], "wb+") as f:
    im = Image.open(sys.argv[1])
    pixel = im.load()
    (width, height) = im.size
    length,markX,markY = findlength(width,height)

    #calculate coordinates of all identity points
    firstX = markX - length - 1
    firstY = markY + 2

    secondX = markX - 2
    secondY = firstY

    thirdX = firstX
    thirdY = firstY + length - 1

    fourthX = secondX
    fourthY = thirdY

    for y in range(firstY,thirdY+1):
        for x in range(firstX,secondX+1):
            r,g,b = pixel[x,y][0:3]
            #recobmine data from r,g,b
            #0xabc00000, 0xdef00000, 0xgh000000 -> 0xabcdefgh
            newFileBytes = [int(r)|int(g)>>3|int(b)>>6]
            if newFileBytes!=[0]: f.write(bytearray(newFileBytes))
