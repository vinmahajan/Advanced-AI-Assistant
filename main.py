from AI_Brains import Google_Gemini
import speech_recognition as sr
import pyttsx3 

# print(Google_Gemini.Ask_Gemini("what is ohms law"))


# Python program to translate
# speech to text and text to speech




# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    
    
# Loop infinitely for user to
# speak

while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            # r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input
            print("Listening...") 
            audio2 = r.listen(source2)
            
            try:
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
            except:
                MyText = ""
            # Activation_Prompts = ["hey mini", "hi mini", "wake up mini", "]

            # if(MyText !=""):
            if("mini" in MyText.split(" ")):
                print(MyText)
                # SpeakText(MyText)
            
    except sr.RequestError as e:
        print("Could not request results format",e)
        
    except sr.UnknownValueError:
        print("unknown error occurred")
