import cv2
import numpy as np
from pyzbar.pyzbar import decode

def main():
    vid_cap = cv2.VideoCapture(0)
    #img = cv2.imread('resources/barode3.jpg')
    while(True):
        ret, img = vid_cap.read()
        h = img.shape[0]
        w = img.shape[1]
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            print(myData)
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,255),2)
            pts2 = barcode.rect
            cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),1)
        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()