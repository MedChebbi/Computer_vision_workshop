import cv2
import numpy as np

#creating an empty image of zeros with 400 lines 500 columns 
####[CODE HERE]####

#replacing the RGB values of the image all white
####[CODE HERE]####

#converting it to colored so we can draw colorful text and drawings
imgRaw = cv2.cvtColor(imgRaw,cv2.COLOR_GRAY2BGR)
#draw whatever you want using cv2.line(), cv2.arrowedLine(), cv2.rectangle(), cv2.circle() and cv2.putText() on imgRaw
####[CODE HERE]####


#Show results
cv2.imshow('result', imgRaw)
cv2.waitKey(0)