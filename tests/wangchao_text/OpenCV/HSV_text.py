import cv2
import numpy as np

img = cv2.imread("R-C.jpg")
if img is None:
    print("图片读取失败！检查文件名")
else:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([15, 100, 120])
    upper_yellow = np.array([32, 255, 255])
   
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imwrite("mask_nailong.png", mask)
    cv2.imwrite("split_result_nailong.png", result)
    print("✅运行完成！生成 mask_nailong.png 和 split_result_nailong.png")