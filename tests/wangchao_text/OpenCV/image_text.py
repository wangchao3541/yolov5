import cv2
import numpy as np

img = cv2.imread("apple.image.jpg",cv2.IMREAD_GRAYSCALE)
if img is None:
    print("读取失败！找不到图片")
else:
    print("读取成功，图像形状：", img.shape)
    cv2.imshow("apple", img)
    cv2.waitKey(0)
    cv2.imwrite("out.jpg", img)