import cv2
import numpy as np


img_path = '../resources/images/lena.png'
save_path = '../resources/images/lena_resized.png'
#Reading image
img = cv2.imread(img_path)
# Extract image dimensions
w , h , c = img.shape
#Resizing image: cv2.resize()
####[CODE HERE]####

#converting image color: cv2.cvtColor(), to switch color spaces we can use costants such as cv2.COLOR_BGR2GRAY
####[CODE HERE]####

#Cropping image: Deal with the image as if it's an nd array
####[CODE HERE]####
#cropped_img = 
#Brightness and contrast change
new_image = cv2.convertScaleAbs(img, alpha=0.75, beta=-30)
#Showing results
cv2.imshow('img',img)
cv2.imshow('gray-img',gray_img)
cv2.imshow('cropped-img',cropped_img)
cv2.imshow('inv_img', inv_img)
cv2.waitKey(0)

