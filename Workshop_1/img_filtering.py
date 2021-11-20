import cv2
import numpy as np


img_path = '../resources/images/noisy_lena.jpg'

#Reading image
img = cv2.imread(img_path)
#Noise removal
# Blur the image
#img_blur = cv2.blur(img,(3,3))
img_blur = cv2.GaussianBlur(img, (5,5),0)  #cv2.
img_blur_2 = cv2.medianBlur(img, 5)
kernel = np.ones((5,5),np.uint8)
# Edge Detection
edges = cv2.Canny(img_blur, 20, 350)
lap = cv2.Laplacian(img_blur, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

# pixel noise removal
erosion = cv2.erode(edges,kernel,iterations = 2)
dilation = cv2.dilate(edges,kernel,iterations = 2)
#Sharpenning
#Define the sharpenning filter
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
#Applying conv operation
image_sharp = cv2.filter2D(img, ddepth=-1, kernel=kernel)
#Showing results
cv2.imshow('blured', img_blur)
cv2.imshow('edges', edges)
cv2.imshow('sharp', image_sharp)
cv2.imshow('laplacien Edge Detection', lap)
cv2.imshow('img',img)
cv2.waitKey(0)

