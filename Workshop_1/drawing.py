import cv2
import numpy as np

<<<<<<< HEAD
#creating an empty image of zeros with 400 lines 500 columns 
####[CODE HERE]####
imgRaw = np.zeros(400,500)
#replacing the RGB values of the image all white
####[CODE HERE]####
=======

imgRaw = np.zeros((400,500), np.uint8) #creating an empty image of zeros with 400 lines 500 columns 
>>>>>>> tested

#converting it to colored so we can draw colorful text and drawings
imgRaw = cv2.cvtColor(imgRaw,cv2.COLOR_GRAY2BGR)
#draw whatever you want using cv2.line(), cv2.arrowedLine(), cv2.rectangle(), cv2.circle() and cv2.putText() on imgRaw
<<<<<<< HEAD
####[CODE HERE]####


=======
#code here:
cv2.putText(imgRaw,"hello",(200,100),cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0,0,255), 2)
#cv2.rectangle(imgRaw,(40,40),(200,400),(255,0,0),2)
#cv2.circle(imgRaw,(300,100),50,(0,255,0),cv2.FILLED)
#cv2.line(imgRaw,(100,100),(200,400),(0,255,0),2)
cv2.arrowedLine(imgRaw,(100,100),(200,400),(0,255,0),2)
#end
>>>>>>> tested
#Show results
cv2.imshow('result', imgRaw)
cv2.waitKey(0)