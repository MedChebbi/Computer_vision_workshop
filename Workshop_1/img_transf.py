import cv2
import numpy as np


img_path = '../resources/images/lena.png'

#Reading image
img = cv2.imread(img_path)

#Affine transformations
#Flip
flipped_img = cv2.flip(img, 1)
#Rotate
rot_img = cv2.rotate(img, cv2.ROTATE_180)
#Zoom
    
#Translate

#Showing results
cv2.imshow('img',img)
cv2.imshow('inv_img', flipped_img)
cv2.imshow('rot_img', rot_img)
cv2.waitKey(0)
