import argparse
from ultralytics import YOLO

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="test.jpg")
    ap.add_argument("--model", default="yolov8n.pt")
    ap.add_argument("--conf", type=float, default=0.25)
    ap.add_argument("--iou", type=float, default=0.45)
    args = ap.parse_args()

    model = YOLO(args.model)
    r = model(args.source, conf=args.conf, iou=args.iou, verbose=False)[0]

    n = len(r.boxes)
    print(f"检测到 {n} 个目标 | 原图 {r.orig_shape}")
    for i in range(n):
        x1, y1, x2, y2 = r.boxes.xyxy[i].tolist()
        conf = float(r.boxes.conf[i])
        cls = int(r.boxes.cls[i])
        print(f"[{i}] {r.names[cls]:12s} conf={conf:.3f} "
              f"box=({x1:.1f},{y1:.1f},{x2:.1f},{y2:.1f})")
    print("speed(ms):", r.speed)
    r.save(filename="out.jpg")

if __name__ == "__main__":
    main()