import cv2
import numpy as np

imgOrange = cv2.imread('../resources/images/orange.jpg')
imgOrange = cv2.resize(imgOrange, (imgOrange.shape[1]//2,imgOrange.shape[0]//2))
imgOrangeCopy = imgOrange.copy()

#Apply the canny filter to get the edges of the Orange image:
imgCanny = cv2.Canny(imgOrangeCopy,100,300)

#Finding contours
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#Going through all the contours and filtering out using are
for cnt in contours:
    area = cv2.contourArea(cnt)
    cv2.drawContours(imgOrangeCopy, cnt, -1, (255, 0, 255),3)
    if area > 400:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        x , y , w, h = cv2.boundingRect(approx)
        cv2.rectangle(imgOrangeCopy, (x , y ), (x + w , y + h ), (0, 255, 0), 5)

#Show results
cv2.imshow('result', imgOrangeCopy)
cv2.waitKey(0)