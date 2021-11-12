import cv2
import numpy as np

def cluster_det(img_gray):
    filtered_cnts = []
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
    kernel = np.ones((3,3),np.uint8)
    # Canny Edge Detection
    edges = cv2.Canny(img_blur, 20, 350)
    lap = cv2.Laplacian(img_blur, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    #cv2.imshow('laplacien Edge Detection', lap)
        
    sobelX = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobelCombined = cv2.bitwise_or(sobelX, sobelY)
    sum_edges = cv2.bitwise_or(sobelCombined, edges)
    final_edges = cv2.bitwise_or(sum_edges, lap)
    erosion = cv2.erode(final_edges,kernel,iterations = 2)
    dilation = cv2.dilate(final_edges,kernel,iterations = 2)

    opening = cv2.morphologyEx(final_edges, cv2.MORPH_OPEN, kernel)
    
    contours, hierarchy = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            filtered_cnts.append(cnt)
    #cv2.imshow('sobelCombined Edge Detection', sobelCombined)
    cv2.imshow('final_edges Edge Detection', final_edges)
    # Display Canny Edge Detection Image
    #cv2.imshow('Canny Edge Detection', edges)
    #cv2.imshow('img_blur', img_blur)
    cv2.imshow('opening', dilation)   
    return filtered_cnts
    
def main():
    return None

if __name__ == '__main__':
    main()