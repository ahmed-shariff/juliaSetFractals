#import cv2;
import numpy as np
from math import exp
from math import sin
from math import cos

height = 1000
width = int(height* 16/9)

area = 3
areaX = area * 16/9
xshift = 0
yshift = 0

paletteSize = 200
radius = 5
colorScheme = 4

minX = -(areaX/2) + xshift
maxX = areaX/2 + xshift
minY = -(area/2) + yshift
maxY = area/2 + yshift

stepX = (maxX - minX) / width
stepY = (maxY - minY) / height

black = [0,0,0]
white = [120,120,120]
red = [0,0,255]



img = np.zeros([height,width,3])*150
l = []

def calculateColor(x, y, palette):
    re = x
    im = y
    for i in range(paletteSize):
        tempRe = re*re - im*im + 0.285
        im = 2* re* im + 0.01
        re = tempRe
        # tempRe = re*re*re - 3*re*im*im;
        # im = 3*re*re*im - im*im*im;
        # re = tempRe;
      
        # try:
        #     tempRe = exp(re) * cos(im) - 0.621
        
        #     im = exp(re) * sin(im)
        #     re = tempRe
        # except:
        #     im = radius
        #     re = radius
        #l.append([re,im])

        
        if re*re + im*im > radius:
            #print(re*re + im*im > radius)
            #print("\t\tadsfhkjasdfkjh    {0} {1} {2}".format(re, im, radius))
            return palette[i]
    return white

def rampFunc(i, IncRange):
    i = i*IncRange
    return [i,i,i]


def createPalette():

    ################################################
    rampLvl = 1
    secDivision = 1
    top = 255 #255
    ################################################

    palette = [[0 for pSize in range(3)] for y in range(paletteSize)]
    inRange = int(paletteSize/4)
    fullIncRange = top/inRange
    halfIncRange = top/(inRange*2)
    lvl1 = inRange
    lvl2 = inRange * 2
    lvl3 = inRange * 3
    secDivInRange = secDivision*inRange
    isecDivInRange = (1-secDivInRange)*inRange

    if colorScheme is 5:
        for i in range(paletteSize):
            val = i*255/paletteSize
            palette[i] = [val, val, val]
        
    else:
        for i in range(inRange):
            if colorScheme is 1:
                palette[i][0] = fullIncRange * i
                palette[i][1] = 128-halfIncRange*i
                palette[i][2] = 255-fullIncRange*i
            elif colorScheme is 2:
                palette[i][0] = 0;
                palette[i][1] = 0;
                palette[i][2] = 0;
            elif colorScheme is 3:
                if rampLvl is 1:
                    palette[i] = rampFunc(i, fullIncRange)
                else:
                    palette[i] = red
            elif colorScheme is 4:
                palette[i][2] = i*fullIncRange
                if i > secDivInRange:
                    palette[i][0] = (secDivision-(i-secDivInRange)*secDivision/isecDivInRange)*top
                    #(0.8*inRange-((i-0.8*inRange)/0.2)* 0.4)*fullIncRange
                    palette[i][1] = (secDivision-(i-secDivInRange)*secDivision/isecDivInRange)*top
                    #fullIncRange*(0.8-0.2*(i-0.8*inRange)/0.2*inRange)
                else:
                    palette[i][0] = i*fullIncRange;
                    palette[i][1] = i*fullIncRange;
        for i in range(inRange):
            if colorScheme is 1:
                palette[i+lvl1][0] = 255
                palette[i+lvl1][1] = fullIncRange * i
                palette[i+lvl1][2] = 0
            elif colorScheme is 2:
                palette[i+lvl1][0] = 0;
                palette[i+lvl1][1] = 255;
                palette[i+lvl1][2] = 255;
            elif colorScheme is 3:
                if rampLvl is 2:
                    palette[i+lvl1] = rampFunc(i, fullIncRange)
                else:
                    palette[i+lvl1] = red
            elif colorScheme is 4:
                palette[i+lvl1][0] = top-60 - i * halfIncRange
                palette[i+lvl1][1] = top-60 - i * fullIncRange
                palette[i+lvl1][2] = top-20 - i * halfIncRange * 0.4
        for i in range(inRange):
            if colorScheme is 1:
                palette[i+lvl2][0] = 128-halfIncRange*i
                palette[i+lvl2][1] = 255
                palette[i+lvl2][2] = fullIncRange*i
            elif colorScheme is 2:
                palette[i+lvl2][0] = 0;
                palette[i+lvl2][1] = 255;
                palette[i+lvl2][2] = 0;
            elif colorScheme is 3:
                if rampLvl is 3:
                    palette[i+lvl2] = rampFunc(i, fullIncRange)
                else:
                    palette[i+lvl2] = red
            elif colorScheme is 4:
                palette[i+lvl2][0] = 0;
                palette[i+lvl2][1] = i*fullIncRange;
                palette[i+lvl2][2] = i*fullIncRange;
        for i in range(inRange):
            if colorScheme is 1:
                palette[i+lvl3][0] = i*fullIncRange
                if i > inRange*0.1:
                    palette[i+lvl3][1] = 0.8*fullIncRange*(1-(i-0.8*fullIncRange)/0.2*fullIncRange)
                    palette[i+lvl3][2] = fullIncRange*(0.8-0.2*(i-0.8*fullIncRange)/0.2*fullIncRange)
                else:
                    palette[i+lvl3][1] = i*fullIncRange;
                    palette[i+lvl3][2] = i*fullIncRange;
            elif colorScheme is 2:
                palette[i+lvl3][0] = 0;
                palette[i+lvl3][1] = 0;
                palette[i+lvl3][2] = 255;
            elif colorScheme is 3:
                if rampLvl is 4:
                    palette[i+lvl3] = rampFunc(i, fullIncRange)
                else:
                    palette[i+lvl3] = red
            elif colorScheme is 4:
                palette[i+lvl3][0] = i*halfIncRange
                palette[i+lvl3][1] = i*fullIncRange
                palette[i+lvl3][2] = top/2 + i*halfIncRange
    return palette


def genImg(img):
    l = []
    palette = createPalette()
    for y in range(height-1, 0, -1):
        #print(y)
        for x in range(width-1):
            #print("{0} {1}".format(x,y))
            color = calculateColor( (x*stepX)+minX, (y*stepY)+minY, palette)
            #print("{0} {1} {2} {3} {4}".format(x_,y_,color,x,y))
            img[y,x,0] = color[0]
            img[y,x,1] = color[1]
            img[y,x,2] = color[2]

    return img
