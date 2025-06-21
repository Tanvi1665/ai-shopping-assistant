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

- Python  
- YOLOv5 (via `torch.hub`)  
- OpenCV – camera capture  
- SpeechRecognition – voice input  
- Pyttsx3 – text-to-speech  
- Pandas, Seaborn – used by YOLO internally  

---

## 📂 Project Structure

ai_shopping_assistant/
├── main_app.py # Main script to run the assistant
├── camera.py # Captures webcam image
├── tts.py # Converts text to speech
├── voice_input.py # Handles microphone input
├── object_detection.py # YOLOv5 object detection logic
├── product_info.py # Product details dictionary
├── requirements.txt # Python dependencies
└── README.md # Project description

yaml
Copy
Edit

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-shopping-assistant.git
cd ai-shopping-assistant
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Note: If pyaudio fails to install (common on Windows), download a prebuilt .whl file from:

🔗 https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Then install it using:

bash
Copy
Edit
pip install path-to-downloaded.whl
🧪 Run the App
bash
Copy
Edit
python main_app.py
Say: What is in front of me
✅ The assistant will identify the object and speak its name and info.

🧠 Future Improvements
Add multiple object detection at once

Loop-based interaction for continuous shopping

Integrate real-time product data from online APIs (e.g., Amazon, Flipkart)

Mobile version using Flask or Kivy
