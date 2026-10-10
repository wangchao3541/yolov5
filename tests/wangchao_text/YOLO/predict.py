from ultralytics import YOLO
model = YOLO("/home/wangchao/catkin_ws/src/plumbing_pub_sub/YOLO/model_maker/runs/detect/train-4/weights/best.pt")
img_path = "/home/wangchao/catkin_ws/src/plumbing_pub_sub/YOLO/helu_desert/final__text.jpg"
results = model(img_path,
                save=True,
                conf=0.5,
                project="/home/wangchao/catkin_ws/src/plumbing_pub_sub/YOLO/output")
for res in results:
    boxes = res.boxes
    print("检测到的框：", boxes)
    print("类别编号：", boxes.cls)
    print("置信度：", boxes.conf)