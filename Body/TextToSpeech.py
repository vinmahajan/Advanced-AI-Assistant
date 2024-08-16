import pyttsx3

def text_to_speech(text):
    print("Speaking: " + text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
