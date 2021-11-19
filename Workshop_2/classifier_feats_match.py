import cv2


path = '../resources/images/'
template_paths = [path+'lion.png',path+'monkey.png',path+'giraffe.png']
template_images = []
class_names = ['Lion', 'Monkey', 'Giraffe']

for img_path in template_paths:
    current_img = cv2.imread(img_path,0)
    template_images.append(current_img)


orb = cv2.ORB_create(nfeatures=800)
matcher = cv2.BFMatcher()


def extract_features(images):
    feats_list = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        feats_list.append(des) 
    return feats_list


def classify(imgGray, img, feats_list, thres=20):
    kp2, des2 = orb.detectAndCompute(imgGray, None)
    match_list = []
    class_id = -1
    try:
        for feats in feats_list:
            matches = matcher.knnMatch(feats,des2, k=2)
            good_matches = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good_matches.append([m])
            match_list.append(len(good_matches))
        print(match_list)
        
        if len(match_list)>0:
            if max(match_list)>thres:
                class_id = match_list.index(max(match_list))
    except:
        print('no matches found')
    if class_id!=-1:
        cv2.putText(img, class_names[class_id],(20,20),cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 1)
    return class_id


img = cv2.imread('../resources/images/full_image.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
feats_list = extract_features(template_images)
id = classify(imgGray, img, feats_list) 

cv2.imshow("result",img)
cv2.waitKey(0)


# From camera test
'''
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        id = classify(imgGray, frame, feats_list) 

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
# Closes all the frames
cv2.destroyAllWindows()
'''