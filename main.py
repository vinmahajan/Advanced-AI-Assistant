import configparser
from AI_Brains import Google_Gemini
from Body import Audio_Engine
import json

# reading AI name from configuration settings
config = configparser.ConfigParser()
config.read('config.ini')
AI_NAME = config['DEFAULT']['AI_NAME']
USER_NAME = config['DEFAULT']['USER_NAME']

# read the greeting codes json file and replace the AI name
def load_greeting_codes(ai_name, user_name):
    with open("Data/Greeting_codes.json", 'r') as file:
        greeting_codes = json.load(file)

    # Replace the placeholder with the actual AI name
    for category, phrases in greeting_codes.items():
        greeting_codes[category] = {phrase.replace("{AI_NAME}", ai_name).replace("{USER_NAME}", user_name): response for phrase, response in phrases.items()}

    return greeting_codes

greeting_codes = load_greeting_codes(AI_NAME, USER_NAME)



# start up greeting
Audio_Engine.text_to_speech(f"Hello, I'm {AI_NAME} your personal AI assistant.")


while True:
    print("loop........................................................\n")
    # greet back if user greet
    Text = Audio_Engine.SpeechRecognizer()
    print(Text)
    if (Text in greeting_codes["Greeting"].keys()):
        print("Greetings.")
        Audio_Engine.text_to_speech(greeting_codes["Greeting"][Text])
        # listening after greeting
        Text += " "
        print("listenning.")
        NText = Audio_Engine.SpeechRecognizer()
        while len(NText) < 5:
            print(".")
            NText = Audio_Engine.SpeechRecognizer()
 
        Text += NText
        print(Text)
    
    
    
    # Aborting the current recognition
    if(Text in greeting_codes["Abort"].keys()):
        print("Aborted.")
        Audio_Engine.text_to_speech(greeting_codes["Abort"][Text])
        
    
    # shut down the recognition
    elif(Text in greeting_codes["Shutdown"].keys()):
        Audio_Engine.text_to_speech(greeting_codes["Shutdown"][Text])
        print("signing off")
        break


    # ask to AI if prompt if valid
    elif(AI_NAME in Text and len(Text) > 15):
        print("ask gemini",Text)
        # ask ai  
        # response = Google_Gemini.Ask_Gemini(Text, AI_NAME)
        # if(len(response[AI_NAME]) > 5):
        #     Audio_Engine.text_to_speech(response[AI_NAME])
        

        # beta
        # if ("Task1" in list(response.keys())):
        #     if (response["Task1"]["Action"] in Action_list):
        #         response["Task1"]["ActionValue"]
            
    elif(AI_NAME in Text and len(Text) < 15):
        Audio_Engine.text_to_speech("sorry, i could not recognize it, please say it again.")
