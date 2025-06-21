# tts.py
import pyttsx3

def speak(text):
    print("🔊 Speaking:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
