import cv2
import numpy as np
from pyzbar.pyzbar import decode


<<<<<<< HEAD
img = cv2.imread('../resources/images/qr_1.png')
h = img.shape[0]
w = img.shape[1]
for barcode in decode(img):
    myData = barcode.data.decode('utf-8')
    print(myData)
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(255,0,255),2)
    pts2 = barcode.rect
    #Add text of the QR code reading
    ####[CODE HERE]####
    
cv2.imshow("image", img)
cv2.waitKey(0) 
=======
####### On image  #######
# img = cv2.imread('../resources/images/monkey.png')
# h = img.shape[0]
# w = img.shape[1]
>>>>>>> tested

# for barcode in decode(img):
#     myData = barcode.data.decode('utf-8')
#     print(myData)
#     pts = np.array([barcode.polygon],np.int32)
#     pts = pts.reshape((-1,1,2))
#     cv2.polylines(frame,[pts],True,(255,0,255),2)
#     pts2 = barcode.rect
#     cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),1)
# cv2.imshow("image", frame)
    
    

######## On video #######
vid_cap = cv2.VideoCapture(0)

while(True):
    ret, img = vid_cap.read()
    h = img.shape[0]
    w = img.shape[1]
    print(decode(img))
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),2)
        pts2 = barcode.rect
        print(pts2)
        #cv2.rectangle(img,(pts2["left"],,pts2[1],(0,255,0),2)
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),1)
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid_cap.release()
cv2.destroyAllWindows()