import pyttsx3

def text_to_speech(text, rate=174, volume=1.0, voice_index=1):
    """Convert text to speech with specified voice."""
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty('rate', rate)  # Speed of speech
    engine.setProperty('volume', volume)  # Volume level (0.0 to 1.0)

    # Get and set the voice by index
    voices = engine.getProperty('voices')
    if voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    else:
        print(f"Voice index {voice_index} is out of range. Using default voice.")

    engine.say(text)
    engine.runAndWait()

# if __name__ == "__main__":

#     text = "Hello, this is a fast and customizable text-to-speech conversion."
#     text_to_speech(text, voice_index=1)
