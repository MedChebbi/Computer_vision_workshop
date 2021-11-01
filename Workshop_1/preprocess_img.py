import cv2
import numpy as np

def main():
    img_path = '../resources/lena.png'
    save_path = '../resources/lena_resized.png'
    #Reading image
    img = cv2.imread(img_path)
    #converting image color
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    inv_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #Cropping image
    cropped_img = img[100:,200:]
    #Brightness and contrast change
    new_image = cv2.convertScaleAbs(img, alpha=0.75, beta=-30)
    #Showing results
    cv2.imshow('img',img)
    cv2.imshow('gray-img',gray_img)
    cv2.imshow('inv_img', inv_img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()