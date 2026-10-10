import cv2
img = cv2.imread("people.jpg")
if img is None:
    print("图片读取失败")
else:
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), thickness=2)

    cv2.imwrite("face_result.png", img)
    print("检测完成，图片已保存")
