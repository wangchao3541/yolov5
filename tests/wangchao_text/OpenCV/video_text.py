import cv2
import numpy as np
vc=cv2.VideoCapture("video_text.mp4")
height=int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
width=int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out=cv2.VideoWriter("gray_video.avi",fourcc,20,(width,height))
if vc.isOpened():
    ret,frame=vc.read()
    open=True
else:
    open=False

while open:
    ret,frame=vc.read()
    if frame is None:
        break
    if ret:
        vc_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray_video",vc_gray)
        gray_vc=cv2.cvtColor(vc_gray,cv2.COLOR_GRAY2BGR)
        out.write(gray_vc)
        if cv2.waitKey(20) & 0xff==27:
           break
out.release()
vc.release()
cv2.destroyAllWindows()

    
