import cv2
import numpy as np


img_path = '../resources/images/lena.png'
save_path = '../resources/images/lena_gray.png'
#Reading image: we will be using cv2.imread()
####[CODE HERE]####
img = cv2.imread(img_path)
print(img.shape)
h , w , c = img.shape
print('image height: ', h)
print('image width: ', w)
#Saving image: we will be using cv2.imwrite() method
####[CODE HERE]####
cv2.imwrite(save_path, img)
#Showing images: cv2.imshow()
####[CODE HERE]####
cv2.imshow("img",img)
cv2.waitKey(0)