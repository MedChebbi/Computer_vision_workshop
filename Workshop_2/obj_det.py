import cv2
import numpy as np


THRES = 0.4 # Threshold to detect object
NMS_THRE = 0.2
RED = (0,0,255)
BLUE = (255,0,0)
GREEN = (0,255,0)

class_names= []
classFile = '../resources/models/object_detection_classes_coco.txt'
with open(classFile,'rt') as f:
  class_names = f.read().rstrip('\n').split('\n')

# Get a different colors for each of the classes
colors = np.random.uniform(0, 255, size=(len(class_names), 3))

def getObject(img, model , draw = True):

    objsInfo = []
    imgHeight, imgWidth, channels = img.shape
    # Make forward pass in model
    output = model.forward()
    # Run over each of the detections
    for detection in output[0,0,:,:]:
        objsInfo.append(detection)
        confidence = detection[2]

        if confidence > THRES:

            class_id = detection[1]

            class_name = class_names[int(class_id)-1]
            color = colors[int(class_id)]

            bboxX = detection[3] * imgWidth
            bboxY = detection[4] * imgHeight

            bboxWidth = detection[5] * imgWidth
            bboxHeight = detection[6] * imgHeight

            cv2.rectangle(img, (int(bboxX), int(bboxY)), (int(bboxWidth), int(bboxHeight)),color, thickness=2)

            cv2.putText(img, class_name, (int(bboxX), int(bboxY - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    
    return img, objsInfo

def main():
 
    configPath = '../resources/models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt'
    weightsPath = '../resources/models/frozen_inference_graph.pb'

    raw_img = cv2.imread('../resources/images/image_2.jpg')
    model = cv2.dnn.readNet(model = weightsPath, config = configPath, framework='TensorFlow')

    blob = cv2.dnn.blobFromImage(image=raw_img, size=(300, 300), mean=(104, 117, 123), swapRB=True)
  
    model.setInput(blob)
    # forward pass through the model to carry out the detection
    
    img, objectsInfo = getObject(raw_img, model)
    cv2.imshow("result", img)
    cv2.waitKey(0)
    #print(objectsInfo)

if __name__ == '__main__':
    main()