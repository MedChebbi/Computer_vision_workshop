import cv2
import numpy as np

def nothing(x):
    pass


def initialize_trackbars():
    #initialize trackbar gui
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 100, 100)
    intialTracbarValueMin = 0 
    intialTracbarValueMax = 50 
    maxValue = 255
    maxValueHue = 180
    cv2.createTrackbar("min_Hue", "Trackbars", intialTracbarValueMin,maxValueHue , nothing)
    cv2.createTrackbar("min_Saturation", "Trackbars", intialTracbarValueMin ,maxValue, nothing)
    cv2.createTrackbar("min_Value", "Trackbars", intialTracbarValueMin ,maxValue, nothing)
    cv2.createTrackbar("max_Hue", "Trackbars", intialTracbarValueMax,maxValueHue , nothing)
    cv2.createTrackbar("max_Saturation", "Trackbars", intialTracbarValueMax, maxValue, nothing)
    cv2.createTrackbar("max_Value", "Trackbars", intialTracbarValueMax, maxValue, nothing)

def extract_values():
    min_H = cv2.getTrackbarPos("min_Hue", "Trackbars")
    max_H = cv2.getTrackbarPos("max_Hue", "Trackbars")
    min_S = cv2.getTrackbarPos("min_Saturation", "Trackbars")
    max_S = cv2.getTrackbarPos("max_Saturation", "Trackbars")
    min_V = cv2.getTrackbarPos("min_Value", "Trackbars")
    max_V = cv2.getTrackbarPos("max_Value", "Trackbars")
    return np.array([min_H,min_S,min_V]), np.array([max_H,max_S,max_V])


greenBGR = np.uint8([[[50,50,50]]])
hsv_green = cv2.cvtColor(greenBGR,cv2.COLOR_BGR2HSV)
print (hsv_green)

img = cv2.imread('../resources/images/colors.png')
img_copy = img.copy()
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#Black approx range in hsv: (0, 0, 0) ~ (180, 255, 30)
#White approx range in hsv: (0, 0, 180) ~ (180, 0, 255)
#Green approx range in hsv: (40, 40,40) ~ (70, 255,255)
#Red approx range in hsv: (10, 100, 20) ~ (25, 255, 255)
#Blue approx range in hsv: (110,150,50) ~ (120,255,255)
initialize_trackbars()

while True:
    min_values, max_values = extract_values()
    maskHSV = cv2.inRange(imgHSV,min_values,max_values)
    kernel = np.ones ((3,3), np.uint8)
    #imgEroded = cv2.erode(maskHSV, kernel, iterations=3)
    #imgDilated = cv2.dilate(imgEroded, kernel, iterations=3) #we used those filters to smooth the mask for a better detection
    
    res = cv2.bitwise_and(img,img, mask= maskHSV)
    contours, hierarchy = cv2.findContours(maskHSV, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(img_copy, cnt, -1, (255, 0, 255),3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv2.boundingRect(approx)
            cv2.rectangle(img_copy, (x , y ), (x + w , y + h ), (0, 255, 0), 3)
    #Show results
    cv2.imshow('result', img)
    cv2.imshow('result_final', img_copy)
    cv2.imshow('result2', res)
    cv2.imshow('mask', maskHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break