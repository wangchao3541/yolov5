from ultralytics import YOLO
if __name__=="__main__":
    model=YOLO("yolo11n")
    model.train(
        data="/home/wangchao/catkin_ws/src/plumbing_pub_sub/YOLO/helu_desert/hulu.yaml",
        epochs=10,
        imgsz=640,
        batch=2,
        cache=False,
        workers=0,
    )