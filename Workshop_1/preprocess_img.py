import cv2
import numpy as np

def main():
    img_path = '../resources/lena.png'
    save_path = '../resources/lena_resized.png'
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    inv_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    cv2.imshow('img',img)
    cv2.imshow('gray-img',gray_img)
    cv2.imshow('inv_img', inv_img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()