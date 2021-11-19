import cv2
import numpy as np


img_path = '../resources/images/lena.png'
save_path = '../resources/images/lena_gray.png'
img = cv2.imread(img_path, 0)
print(img.shape)
w , h , c = img.shape
print('image height: ', h)
print('image width: ', w)
#Saving image
cv2.imwrite(save_path, img)
#Showing images
cv2.imshow('image',img)
cv2.imshow('resized_image',img)
cv2.waitKey(0)
