import cv2
import numpy as np

def main():
    img_path = '../resources/lena.png'
    save_path = '../resources/lena_resized.png'
    img = cv2.imread(img_path)
    print(img.shape)
    w , h , c = img.shape
    print('image height: ', h)
    print('image width: ', h)

    resized_img = cv2.resize(img, (w//2, h//2), interpolation=cv2.INTER_AREA)
    cv2.imwrite(save_path, resized_img)
    cv2.imshow('image',img)
    cv2.imshow('resized_image',resized_img)
    cv2.waitKey(0)
    
if __name__ == '__main__':
    main()