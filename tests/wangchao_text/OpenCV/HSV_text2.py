import cv2
import numpy as np
img=cv2.imread("HSV__text2.png")
if img is None:
    print("图片读取失败")
else:
    HSV_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 80])
    upper_red = np.array([8, 255, 255])
    mask_patt1=cv2.inRange(HSV_img,lower_red,upper_red)

    lower_skin = np.array([5, 40, 100])
    upper_skin = np.array([20, 150, 255])
    mask_patt2=cv2.inRange(HSV_img,lower_skin,upper_skin)

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 60])
    mask_patt3=cv2.inRange(HSV_img,lower_black,upper_black)

    mask = cv2.add(mask_patt1, mask_patt2)
    mask = cv2.add(mask, mask_patt3)

    result=cv2.bitwise_and(img,img,mask=mask)

    cv2.imwrite("finally_HSV.png",result)