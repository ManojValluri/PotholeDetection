import cv2
import numpy as np
import pygame
import time
import smtplib
from matplotlib import pyplot as plt

#kmeansclustering
cv2.startWindowThread()
def plt_show(image, title=""):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.axis("off")
    plt.title(title)
#
    plt.imshow(image, cmap=plt.cm.Greys_r)
    plt.show()

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized



img = cv2.imread(r"/Users/Manoj_Valluri/Desktop/AI Project/testk.png")
plt.imshow(img)
plt.show()

Z = img.reshape((-1,3))

Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imwrite(r"/Users/Manoj_Valluri/Desktop/AI Project/testk.png", res2)

cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
