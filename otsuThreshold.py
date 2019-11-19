import cv2
import numpy as np
import pygame
import time
import smtplib
from matplotlib import pyplot as plt


#otsu's thresholding and grayscaling

img = cv2.imread(r"/Users/Manoj_Valluri/Desktop/AI Project/test.png",0)


# Otsu's thresholding
ret,th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [#img, 0, th1,
          img, 0, th,
          #blur, 0, th3
          ]


for i in xrange(1):

    plt.subplot(3,3,i*6+3),plt.imshow(images[i*6+2],'gray')
    plt.savefig("/Users/Manoj_Valluri/Desktop/AI Project/testk.png")
    #plt.title(titles[i*6+2]), plt.xticks([]), plt.yticks([])
plt.show()
