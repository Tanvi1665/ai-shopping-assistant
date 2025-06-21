from voice_input import get_voice_command
from tts import speak
from camera import capture_image
from object_detection import detect_object
from product_info import product_data

def main():
    speak("Hello! I am your shopping assistant.")
    speak("Say 'what is in front of me' to identify an item.")

    command = get_voice_command()

    if "what is in front" in command:
        image_file = capture_image()
        label = detect_object(image_file)

        if label != "nothing":
            if label in product_data:
                info = product_data[label]
                text = f"{info['name']}: {info['price']}. {info['description']}"
                speak(text)
            else:
                speak(f"I see a {label}, but no info is available.")
        else:
            speak("I could not identify any object.")
    else:
        speak("Sorry, I didn't understand your command.")


if __name__ == "__main__":
    main()
