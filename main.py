from AI_Brains import Google_Gemini
from Body import Audio_Engine
import json

            
greeting_codes = {
            "greeting":{
                "hey mini": "yo boss.",
                "hi mini": "hey boss.",
                "wake up mini": "i'm always up boss.",
                "shut up":"my apologies.",
                },
            "Abort" :{
                "exit":"okay.",
                "nothing":"no problem.",
                "leave it":"okay, no problem.",
                },
            "shutdown":{
                "shutdown":"signing off.",
                "shut down":"signing off.",
                "power off":"signing off.",
                },
            }


# start up greeting
Audio_Engine.text_to_speech("Hello, I'm mini your personal AI assistant.")


while True:
    # greet back if user greet
    Text = Audio_Engine.SpeechRecognizer()
    if (Text in greeting_codes.keys()):
        print("Greetings.")
        Audio_Engine.text_to_speech(greeting_codes[Text])
        # listening after greeting
        Text = Audio_Engine.SpeechRecognizer()
    
    
    # Aborting the current recognition
    if(Text in greeting_codes["Abort"].keys()):
        print("Aborted.")
        Audio_Engine.text_to_speech(greeting_codes["Abort"][Text])
        continue
    
    # shut down the recognition
    elif(Text in greeting_codes["shutdown"].keys()):
        Audio_Engine.text_to_speech(greeting_codes["shutdown"][Text])
        print("signing off")
        break


    # ask to AI if prompt if valid
    elif(len(Text) > 15):
        # ask ai  
        response = Google_Gemini.Ask_Gemini(Text)
        if(response["mini"]):
            Audio_Engine.text_to_speech(response["mini"])
        

        # beta
        # if ("Task1" in list(response.keys())):
        #     if (response["Task1"]["Action"] in Action_list):
        #         response["Task1"]["ActionValue"]
            
