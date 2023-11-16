import speech_recognition as sr

import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        print("Listening...")

        try:
            # recognizer.pause_threshold(1)
            audio = recognizer.listen(source, timeout=1)
            print("Recognizing...")

            text = recognizer.recognize_google(audio, language='en-in')
            # print(f"You said: {text}")
            return text

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")

while True:
    speech_text = speech_to_text()

    with open('AI_Brains\cookies\transcribe.txt', 'w') as file:
        file.write(speech_text)
        # print(user_input)
        # if user_input:
        #     text_to_speech(user_input)
