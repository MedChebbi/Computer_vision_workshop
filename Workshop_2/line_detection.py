import cv2
import numpy as np

def nothing(x):
    pass


def initialize_trackbars():
    #initialize trackbar gui
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 400, 400)
    intialTracbarValueMin = 0 
    intialTracbarValueMax = 50 
    maxValue = 255
    maxValueHue = 180
    black = [[0, 0, 0],[180, 255, 30]]
    red = [[0, 200, 20],[15, 255, 255]]
    #Black approx range in hsv: (0, 0, 0) ~ (180, 255, 30)
    #White approx range in hsv: (0, 0, 180) ~ (180, 0, 255)
    #Green approx range in hsv: (40, 40,40) ~ (70, 255,255)
    #Red approx range in hsv: (10, 100, 20) ~ (25, 255, 255)
    #Blue approx range in hsv: (110,150,50) ~ (120,255,255)
    cv2.createTrackbar("min_Hue", "Trackbars", red[0][0],maxValueHue , nothing)
    cv2.createTrackbar("min_Saturation", "Trackbars", red[0][1] ,maxValue, nothing)
    cv2.createTrackbar("min_Value", "Trackbars", red[0][2] ,maxValue, nothing)
    cv2.createTrackbar("max_Hue", "Trackbars", red[1][0],maxValueHue , nothing)
    cv2.createTrackbar("max_Saturation", "Trackbars",red[1][1] , maxValue, nothing)
    cv2.createTrackbar("max_Value", "Trackbars", red[1][2], maxValue, nothing)

def extract_values():
    min_H = cv2.getTrackbarPos("min_Hue", "Trackbars")
    max_H = cv2.getTrackbarPos("max_Hue", "Trackbars")
    min_S = cv2.getTrackbarPos("min_Saturation", "Trackbars")
    max_S = cv2.getTrackbarPos("max_Saturation", "Trackbars")
    min_V = cv2.getTrackbarPos("min_Value", "Trackbars")
    max_V = cv2.getTrackbarPos("max_Value", "Trackbars")
    return np.array([min_H,min_S,min_V]), np.array([max_H,max_S,max_V])


vid_cap = cv2.VideoCapture(0)


greenBGR = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(greenBGR,cv2.COLOR_BGR2HSV)
print (hsv_green)

img = cv2.imread('../resources/images/black.jpg')
img_copy = img.copy()
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

x_c, y_c = img.shape[1]//2, img.shape[0]//2
#Black approx range in hsv: (0, 0, 0) ~ (180, 255, 30)
#White approx range in hsv: (0, 0, 180) ~ (180, 0, 255)
#Green approx range in hsv: (40, 40,40) ~ (70, 255,255)
#Red approx range in hsv: (10, 100, 20) ~ (25, 255, 255)
#Blue approx range in hsv: (110,150,50) ~ (120,255,255)

initialize_trackbars()

while(vid_cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = vid_cap.read()
    x_c, y_c = frame.shape[1]//2, frame.shape[0]//2
    img_copy = frame.copy()
    #imgHSV = frame
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    offset_x = x_c
    min_values, max_values = extract_values()
    maskHSV = cv2.inRange(imgHSV,min_values,max_values)
    kernel = np.ones ((3,3), np.uint8)
    #imgEroded = cv2.erode(maskHSV, kernel, iterations=3)
    #imgDilated = cv2.dilate(imgEroded, kernel, iterations=3) #we used those filters to smooth the mask for a better detection
    
    res = cv2.bitwise_and(frame,frame, mask= maskHSV)
    contours, hierarchy = cv2.findContours(maskHSV, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(img_copy, cnt, -1, (255, 0, 255),3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv2.boundingRect(approx)
            offset_x = x_c - (x+(h//2))
        
            cv2.rectangle(img_copy, (x , y ), (x + w , y + h ), (0, 255, 0), 3)
    cv2.putText(img_copy,str(offset_x),(20,20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0))
    
     
    #Show results
    #cv2.imshow('result', img)
    cv2.imshow('result_final', img_copy)
    cv2.imshow('result2', res)
    cv2.imshow('mask', maskHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break