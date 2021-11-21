import cv2
import numpy as np


img_path = '../resources/images/lena.png'

#Reading image
img = cv2.imread(img_path)
#Noise removal
# Blur the image:there are multiple bluring methods try: cv2.blur(), cv2.GaussianBlur(), cv2.medianBlur()
####[CODE HERE]####
img_blur = cv2.medianBlur(img , 7)
#kernel = np.ones((5,5),np.uint8)
# Edge Detection: cv2.Canny()
####[CODE HERE]####
edges = cv2.Canny(img,100,300)

# pixel noise removal
# erosion = cv2.erode(edges,kernel,iterations = 2)
# dilation = cv2.dilate(erosion,kernel,iterations = 2)
#Sharpenning
#Define the sharpenning filter
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
#Applying conv operation: cv2.filter2D()
####[CODE HERE]####
image_sharp = cv2.filter2D(img,0,kernel)
#Showing results
cv2.imshow('blured', img_blur)
cv2.imshow('edges', edges)
cv2.imshow('sharp', image_sharp)
cv2.imshow('img',img)
cv2.waitKey(0)

