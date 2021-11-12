import cv2
import numpy as np


THRES = 0.50 # Threshold to detect object
NMS_THRE = 0.2
RED = (0,0,255)
BLUE = (255,0,0)
GREEN = (0,255,0)

classNames= []
classFile = 'models/coco.names'
with open(classFile,'rt') as f:
  classNames = f.read().rstrip('\n').split('\n')

def getObject(img, net , draw = True):
  classIds, confs, bbox = net.detect(img, confThreshold = THRES, nmsThreshold = NMS_THRE)
  objsInfo = []

  if len(classIds) != 0:
    for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
      className = classNames[classId - 1]
      objsInfo.append(([box,className]))
 
      if draw:
        cv2.rectangle(img,box,color = GREEN,thickness=2)
        cv2.putText(img,className,(box[0]+10,box[1]+50),
                    cv2.FONT_HERSHEY_COMPLEX,2, GREEN, 2)
        cv2.putText(img,str(round(confidence*100,2)),(box[0]+400,box[1]+50),
                    cv2.FONT_HERSHEY_COMPLEX,2,GREEN ,2)
  return img, objsInfo

def main():
 
  configPath = 'models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
  weightsPath = 'models/frozen_inference_graph.pb'

  net = cv2.dnn_DetectionModel(weightsPath,configPath)
  net.setInputSize(320,320)
  net.setInputScale(1.0/ 127.5)
  net.setInputMean((127.5, 127.5, 127.5))
  net.setInputSwapRB(True)

  raw_img = cv2.imread('resources/Trump.jpg')
  img,objectsInfo = getObject(raw_img)
  print(objectsInfo)

if __name__ == '__main__':
    main()