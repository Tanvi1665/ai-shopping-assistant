# object_detection.py
import torch

# Load YOLOv5 model from Ultralytics repo (first time it downloads weights)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

def detect_object(image_path):
    results = model(image_path)
    df = results.pandas().xyxy[0]  # DataFrame of detections

    if not df.empty:
        label = df.iloc[0]['name']
        print(f"🧠 Detected: {label}")
        return label
    else:
        print("🤷 No object detected.")
        return "nothing"
    
    print(df[['name', 'confidence']])


