# camera.py
import cv2

def capture_image(file_name="captured.jpg"):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Cannot open camera")
        return None

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(file_name, frame)
        print(f"📷 Image saved as {file_name}")
    else:
        print("❌ Failed to capture image")

    cap.release()
    return file_name
