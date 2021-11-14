import cv2


img1 = cv2.imread('../resources/images/full_image.png', 0)
img2 = cv2.imread('../resources/images/lion.png', 0)

orb = cv2.ORB_create(nfeatures=800)
matcher = cv2.BFMatcher()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

img_kp1 = cv2.drawKeypoints(img1,kp1,None)
img_kp2 = cv2.drawKeypoints(img2,kp2,None)
#'''
matches = matcher.knnMatch(des1, des2, k = 2)

good  = []
for m,n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

result = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good, None, flags=2)

cv2.imshow("img_kp1",img_kp1)
cv2.imshow("img_kp2",img_kp2)
#cv2.imshow("img1",img1)
#cv2.imshow("img2",img2)
cv2.imshow("result",result)
cv2.waitKey(0)
#'''

# From camera test
'''
cap = cv2.VideoCapture(2)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp1, des1 = orb.detectAndCompute(imgGray, None)
        img_kp1 = cv2.drawKeypoints(imgGray,kp1,None)
        matches = matcher.knnMatch(des1, des2, k = 2)

        good  = []
        for m,n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])

        result = cv2.drawMatchesKnn(imgGray,kp1,img2,kp2,good, None, flags=2)

        cv2.imshow("img_kp1",img_kp1)
        cv2.imshow("img_kp2",img_kp2)
        cv2.imshow("result",result)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
# Closes all the frames
cv2.destroyAllWindows()
'''