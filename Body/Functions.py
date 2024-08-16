import json
import os


# read the greeting codes json file and replace the AI name
def load_greeting_codes(ai_name, user_name):
    # Body\Data\Greeting_codes.json
    with open("Body/Data/Greeting_codes.json", 'r') as file:
        greeting_codes = json.load(file)

    # Replace the placeholder with the actual AI name
    for category, phrases in greeting_codes.items():
        greeting_codes[category] = {phrase.replace("{AI_NAME}", ai_name): response.replace("{USER_NAME}", user_name) for phrase, response in phrases.items()}
        
    return greeting_codes



def transcript(method="r", write_text=""):
    try:
        while True:
            with open("Body/Transcript/transcript.txt", method) as file:
                # Read the text from the file
                if method == "r":
                    text = file.read()
                    if text:
                        return text
                    
                # clear and write to the file
                elif method == "w":
                    file.write(write_text)
                    break

                # append to the end of the file
                elif method == "a":
                    file.write(write_text)
                    break
    except:
        print(">> failed to read transcript")

def shutdown_computer():
    if os.name == 'nt':
        # For Windows operating system
        os.system('shutdown /s /t 0')
    elif os.name == 'posix':
        # For Unix/Linux/Mac operating systems
        os.system('sudo shutdown now')
    else:
        print('Unsupported operating system.')