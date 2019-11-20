import cv2
import numpy as np
import pygame
import time
import smtplib
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageFilter

#binary switch

im = Image.open(r"/Users/Manoj_Valluri/Desktop/AI Project/testk.png")
pixelMap = im.load()


print pixelMap

img = Image.new( im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
   for j in range(img.size[1]):
       if (0,0,0) == pixelMap[i,j] :
           pixelMap[i,j] = (255,255,255);
       else:
           pixelMap[i,j] = (0,0,0);
im.show()

im.save("/Users/Manoj_Valluri/Desktop/AI Project/testk.png")

#final image

im = Image.open(r"/Users/Manoj_Valluri/Desktop/AI Project/testk.png")
pixelMap = im.load()
im2 = Image.open(r"/Users/Manoj_Valluri/Desktop/AI Project/test.png")
pixelMap2 = im2.load()

#print pixelMap[100,100]

img = Image.new( im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
   for j in range(img.size[1]):
       if (0,0,0) == pixelMap[i,j]:
           continue
       pixelMap2[i,j] = (255,0,0)

im2.show()
im2.save()
