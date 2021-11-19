import cv2
import numpy as np


img_path = '../resources/images/noisy_lena.jpg'

#Reading image
img = cv2.imread(img_path)
#Noise removal

# Blur the image for better edge detection
#img_blur = cv2.blur(img,(3,3))
img_blur = cv2.GaussianBlur(img, (3,3),0)  #cv2.
img_blur_2 = cv2.medianBlur(img, (3,3))
kernel = np.ones((3,3),np.uint8)
# Canny Edge Detection
edges = cv2.Canny(img_blur, 20, 350)
lap = cv2.Laplacian(img_blur, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
#cv2.imshow('laplacien Edge Detection', lap)
        
sobelX = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
sum_edges = cv2.bitwise_or(sobelCombined, edges)
final_edges = cv2.bitwise_or(sum_edges, lap)
erosion = cv2.erode(final_edges,kernel,iterations = 2)
dilation = cv2.dilate(final_edges,kernel,iterations = 2)
#Edge detection

#Sharpenning

#Showing results
cv2.imshow('img',img)
cv2.waitKey(0)

