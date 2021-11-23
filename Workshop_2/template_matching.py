import numpy as np
import cv2

img = cv2.imread('../resources/images/full_monkey.png', 0)
img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
template_monkey = cv2.resize(cv2.imread('../resources/images/monkey.png', 0), (0, 0), fx=0.8, fy=0.8)
template_lion = cv2.resize(cv2.imread('../resources/images/lion.png', 0), (0, 0), fx=0.8, fy=0.8)
template_girraf = cv2.resize(cv2.imread('../resources/images/lion.png', 0), (0, 0), fx=0.8, fy=0.8)

h, w = template_lion.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# for method in methods:
img2 = img.copy()

#Apply template matching
result_lion = cv2.matchTemplate(img2, template_lion, cv2.TM_SQDIFF)
result_monkey = cv2.matchTemplate(img2, template_monkey, cv2.TM_SQDIFF)
#Get difference values and matches
min_val_1, max_val_1, min_loc_1, max_loc_1 = cv2.minMaxLoc(result_lion)
min_val_2, max_val_2, min_loc_2, max_loc_2 = cv2.minMaxLoc(result_monkey)
location_1 = min_loc_1
location_2 = min_loc_2
bottom_right_1 = (location_1[0] + w, location_1[1] + h) 
print(min_val_1)
print(min_val_2)
if min_val_1 < 4000000:
    cv2.putText(img2,"Lion",(20,30), cv2.FONT_HERSHEY_COMPLEX,1,255,1)


cv2.rectangle(img2, location_1, bottom_right_1, 255, 5)
cv2.imshow('Match', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()