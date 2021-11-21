import cv2
import numpy as np


def nothing(x):
    pass


img = cv2.imread('../resources/images/colors.png')
# Convert the image color to the convinient color space
####[CODE HERE]####
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#Let's try figuring out a threshold from a given RGB color
####[CODE HERE]####

#Green approx range in hsv: (40, 40,40) ~ (70, 255,255)
#Red approx range in hsv: (10, 100, 20) ~ (25, 255, 255)
#Blue approx range in hsv: (110,150,50) ~ (120,255,255)
#initialize trackbar gui
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 400, 400)
intialTracbarValueMin = 0 
intialTracbarValueMax = 50 
maxValue = 255
maxValueHue = 180
cv2.createTrackbar("min_Hue", "Trackbars", intialTracbarValueMin,maxValueHue , nothing)
cv2.createTrackbar("min_Saturation", "Trackbars", intialTracbarValueMin ,maxValue, nothing)
cv2.createTrackbar("min_Volume", "Trackbars", intialTracbarValueMin ,maxValue, nothing)
cv2.createTrackbar("max_Hue", "Trackbars", intialTracbarValueMax,maxValueHue , nothing)
cv2.createTrackbar("max_Saturation", "Trackbars", intialTracbarValueMax, maxValue, nothing)
cv2.createTrackbar("max_Volume", "Trackbars", intialTracbarValueMax, maxValue, nothing)

while True:
    min_H = cv2.getTrackbarPos("min_Hue", "Trackbars")
    max_H = cv2.getTrackbarPos("max_Hue", "Trackbars")
    min_S = cv2.getTrackbarPos("min_Saturation", "Trackbars")
    max_S = cv2.getTrackbarPos("max_Saturation", "Trackbars")
    min_V = cv2.getTrackbarPos("min_Volume", "Trackbars")
    max_V = cv2.getTrackbarPos("max_Volume", "Trackbars")

    #Mask colors based on minimum and maximum threshold: use cv2.inRange()
    ####[CODE HERE]####
    maskHSV = cv2.inRange(imgHSV, (min_H,min_S,min_V), (max_H, max_S, max_V))
    #kernel = np.ones ((3,3), np.uint8)
    #imgEroded = cv2.erode(maskHSV, kernel, iterations=3)
    #imgDilated = cv2.dilate(imgEroded, kernel, iterations=3) #we used those filters to smooth the mask for a better detection
    
    #We can fiter out what's not important 
    res = cv2.bitwise_and(img,img, mask= maskHSV)
    #Show results
    cv2.imshow('result', img)
    cv2.imshow('result2', res)
    cv2.imshow('mask', maskHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break