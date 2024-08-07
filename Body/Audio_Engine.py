import speech_recognition as sr
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def SpeechRecognizer():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        try:
            print("Listening...")
            # recognizer.pause_threshold(1)
            audio = recognizer.listen(source, timeout=2)
            print("Recognizing...")

            text = recognizer.recognize_google(audio, language='en-in').lower()
            # print(f"You said: {text}")
            return text

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
    
    return 0

