from ultralytics import YOLO

model = YOLO("yolov8n.pt")      # n = nano，最小的 YOLOv8，项目后面就用它
results = model("test.jpg")       # 首次会自动下载权重；换成你自己的图
results[0].save("out.jpg")       # 保存带框图

r = results[0]
print("检测到框数:", len(r.boxes))     # N
print("原图尺寸:", r.orig_shape)        # (H, W)
print("类别映射:", r.names)             # {0: 'person', ...}
print("xyxy:\n", r.boxes.xyxy)          # (N,4) tensor，像素坐标
print("conf:\n", r.boxes.conf)          # (N,) tensor，置信度
print("cls:\n", r.boxes.cls)            # (N,) tensor，类别 id
print("speed(ms):", r.speed)            # preprocess / inference / postprocess
# import cv2

# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     raise SystemExit("摄像头打不开：检查 /dev/video*、权限、是否被占用")

# ret, frame = cap.read()
# cap.release()
# if not ret:
#     raise SystemExit("read frame fail")


# cv2.imwrite("test.jpg", frame)
# print("saved test.jpg, shape = ", frame.shape)