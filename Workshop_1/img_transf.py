import cv2
import numpy as np


img_path = '../resources/images/image_2.jpg'

#Reading image
img = cv2.imread(img_path)
h , w, c = img.shape
print("width: ",w)
print("height: ",h)
#Affine transformations
#Flip: try cv2.flip()
####[CODE HERE]####
flipped_img = cv2.flip(img,-1)
#Rotate: cv2.rotate()
####[CODE HERE]####
rot_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#Zoom: think about it, you already know the methods to use
####[CODE HERE]####
zoomed_img = img[100:400,100:400]
zoomed_img = cv2.resize(zoomed_img,(w,h))
#Translate
#We define our affine transformation matrix with the format:
#
#	[1, 0, tx]
#	[0, 1, ty]

M = np.float32([
	[1, 0, 25],
	[0, 1, -50]
])
#We translate the image over tx and ty: cv2.warpAffine()
####[CODE HERE]####
shifted = cv2.warpAffine(img,M,(w,h))
#Showing results
cv2.imshow('img',img)
cv2.imshow('inv_img', flipped_img)
cv2.imshow('translated_img',shifted)
cv2.imshow('rot_img', rot_img)
cv2.imshow('zoomed_img', zoomed_img )
cv2.waitKey(0)
