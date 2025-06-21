# 🛍️ AI Shopping Assistant for the Visually Impaired
An AI-powered voice and vision assistant that helps visually impaired individuals identify everyday items through object detection and speech interaction. Built using Python, YOLOv5, and speech recognition technologies.

---
## 🚀 Features
- 🎤 Voice-controlled assistant
- 📷 Real-time object detection using webcam
- 🧠 YOLOv5 deep learning model
- 🔊 Text-to-speech output for item details
- 🛒 Product-specific info: name, price, and description
- ✅ Fully offline-capable

---
## 📸 How It Works
1. User speaks: **"What is in front of me"**
2. The assistant:
   - Captures an image using webcam
   - Detects the most prominent object using YOLOv5
   - Matches it with product information
   - Speaks the item's name, price, and description

---
## 🧠 Tech Stack
- **Python**
- **YOLOv5** (via `torch.hub`)
- **OpenCV** – camera capture
- **SpeechRecognition** – voice input
- **Pyttsx3** – text-to-speech
- **Pandas, Seaborn** – used by YOLO internally

---
## 📂 Project Structure
ai_shopping_assistant/
│
├── main_app.py # Main script to run the assistant
├── camera.py # Captures webcam image
├── tts.py # Converts text to speech
├── voice_input.py # Handles microphone input
├── object_detection.py # YOLOv5 object detection logic
├── product_info.py # Product details dictionary
├── requirements.txt # Python dependencies
└── README.md # Project description

---
## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-shopping-assistant.git
cd ai-shopping-assistant

**2. Install dependencies**
bash
Copy
Edit
pip install -r requirements.txt

⚠️ If pyaudio fails to install (common on Windows), download a prebuilt .whl from
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
and install it with:
bash
Copy
Edit
pip install path-to-downloaded.whl
yaml
Copy
Edit
---

### ✅ Full Section Flow

This version:
- Uses proper code blocks
- Keeps bullet/step style
- Handles `pyaudio` install clearly







