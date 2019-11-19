import cv2
import numpy as np
import pygame
import time
import smtplib
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageFilter


#filtering the clustered image

imageObject = Image.open(r"/Users/Manoj_Valluri/Desktop/AI Project/testk.png");

modeFilterApplied = imageObject.filter(ImageFilter.ModeFilter);

for i in range (0, 4):
    modeFilterApplied = modeFilterApplied.filter(ImageFilter.ModeFilter);

modeFilterApplied.show();
modeFilterApplied.save("/Users/Manoj_Valluri/Desktop/AI Project/testk.png")
