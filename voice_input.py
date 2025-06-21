# voice_input.py
import speech_recognition as sr

def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("✅ You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio.")
        return ""
    except sr.RequestError:
        print("⚠️ Speech service unavailable.")
        return ""
