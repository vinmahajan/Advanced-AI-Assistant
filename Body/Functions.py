import json
import os
import socket


def is_connected():
  try:
    # See if we can resolve the host name - tells us if there is
    # A DNS listening
    host = socket.gethostbyname("one.one.one.one")
    # Connect to the host - tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except Exception:
     pass # We ignore any errors, returning False
  return False



# read the greeting codes json file and replace the AI name
def load_greeting_codes(ai_name, user_name):
    # Body\Data\Greeting_codes.json
    with open("Body/Data/Greeting_codes.json", 'r') as file:
        greeting_codes = json.load(file)

    # Replace the placeholder with the actual AI name
    # for category, phrases in greeting_codes.items():
    #     greeting_codes[category] = {phrase.replace("{AI_NAME}", ai_name): response.replace("{USER_NAME}", user_name) for phrase, response in phrases.items()}
        
    return greeting_codes



def transcript(method="r", write_text=""):
    try:
        while True:
            with open("Body/Transcript/transcript.txt", method) as file:
                # Read the text from the file
                if method == "r":
                    text = file.read()
                    if text:
                        return text.lower().strip()
                    
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