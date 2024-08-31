import configparser
import time
import datetime
import random
import threading
from AI_Brains import Google_Gemini
# from Body.SpeechToText import real_time_stt, LiveSpeechToText
from Body.SpeechToText import LiveSpeechToText
from Body.TextToSpeech import text_to_speech
from Body import Functions
import json


# Create a stop event
stop_event = threading.Event()

# reading AI name from configuration settings
config = configparser.ConfigParser()
config.read('config.ini')
AI_NAME = config['DEFAULT']['AI_NAME']
USER_NAME = config['DEFAULT']['USER_NAME']



def start_thread():
    # stt_thread = threading.Thread(target=real_time_stt, args=(stop_event,))
    stt_thread = threading.Thread(target=LiveSpeechToText, args=(stop_event,))
    stt_thread.start()
        
# get greeting codes
greeting_codes = Functions.load_greeting_codes(AI_NAME, USER_NAME)

if not Functions.is_connected():
    text_to_speech(random.choice(greeting_codes["offline_dlg"]))


# start up greeting
def Timegreet():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        text_to_speech(random.choice(greeting_codes["good_morningdlg"]))
    elif hour >12 and hour<=18:
        text_to_speech(random.choice(greeting_codes["good_afternoondlg"]))
    else:
        text_to_speech(random.choice(greeting_codes["good_eveningdlg"]))
Timegreet()


# start thread for STT
start_thread()








# clear transcript
Functions.transcript(method="w")
while True:
    
    # Read the transcript
    Text = Functions.transcript(method="r")
    # clear transcript
    Functions.transcript(method="w")
    print(Text)

    # greet back if user greet
    if Text in greeting_codes["Greeting"].keys():
        print("Greetings.")
        text_to_speech(greeting_codes["Greeting"][Text])
            
    
    # Aborting the current recognition
    elif Text in greeting_codes["AbortCode"]:
        print("Aborted.")
        stop_event.set()
        text_to_speech(random.choice(greeting_codes["AbortResponse"]))
        exit()

    
    # shut down the recognition
    elif Text in greeting_codes["ShutdownCodes"]:
        text_to_speech(random.choice(greeting_codes["ShutdownResponse"]))
        stop_event.set()
        print("signing off")
        # Functions.shutdown_computer()
        break


    # ask to AI if prompt if valid
    elif AI_NAME in Text[0:20] and len(Text) > 20:
        print("ask AI: ",Text)
        # ask ai  
        # response = Google_Gemini.Ask_Gemini(Text, AI_NAME)
        # if(len(response[AI_NAME]) > 5):
        #     Audio_Engine.text_to_speech(response[AI_NAME])
        

        # beta
        # if ("Task1" in list(response.keys())):
        #     if (response["Task1"]["Action"] in Action_list):
        #         response["Task1"]["ActionValue"]
            
    elif AI_NAME in Text and len(Text) < 20:
        text_to_speech("sorry, i could not recognize it, please say it again.")
