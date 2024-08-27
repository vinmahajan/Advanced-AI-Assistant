import os
import json
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

history_path = "AI_Brains/History/"
date= datetime.now().date()



def getHistory():
    try:
        with open(history_path+str(date)+".txt", "r") as file:
            history = file.read()
    except:
        history=""

    return history




def Ask_llama(query, AI_NAME):
    instruction = "Imagine you are an AI named \""+AI_NAME+"\" that responds like a human. Keep responses brief and always in JSON format. Use the key \""+AI_NAME+"\" for your response, and if tasks are assigned, label them as \"Task1\", \"Task2\", and so on. Each task should include a sub-dictionary with \"Action\" for the task and \"ActionValue\" for its value. \nExample:\nUser command: \"turn on the fan1 and set the speed to 4\"\nYour response: { \""+AI_NAME+"\": \"Ok, turning on the fan and setting speed to 4\", \"Task1\": {\"Action\": \"on_fan1\", \"ActionValue\": \"4\"}}"
    history = getHistory()
    client = Groq(api_key=GROQ_API_KEY)
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[{
                "role": "system",
                "content": instruction
            },
            {
                "role": "user",
                "content":"History: "+history+"\nuser query"+ query
            }

            ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    # Parse the JSON string
    parsed_json = json.loads(response)

    # save the conversation to history file
    context ="{\"role\":\"user\",\"content\":\"" + query + "\"}\n{\"role\":\"model\",\"content\":\"" + str(parsed_json) + "\"},\n"

    
    with open(history_path+str(date)+".txt", "a") as file:
        file.write(context)

    return parsed_json




# response = Ask_llama(text="what is your name", AI_NAME="mini")
# response


# def template(query, AI_NAME):
#     os.makedirs(os.path.dirname(history_path), exist_ok=True)
#     try:
#         with open(history_path+str(date)+".txt", "r") as file:
#             text = json.loads("["+file.read().replace("\n", "").strip(",")+"]")
#     except:
#         text=[]

#     instruction = "Imagine you are an AI named \""+AI_NAME+"\" that responds like a human. Keep responses brief and always in JSON format. Use the key \""+AI_NAME+"\" for your response, and if tasks are assigned, label them as \"Task1\", \"Task2\", and so on. Each task should include a sub-dictionary with \"Action\" for the task and \"ActionValue\" for its value. \nExample:\nUser command: \"turn on the fan1 and set the speed to 4\"\nYour response: { \""+AI_NAME+"\": \"Ok, turning on the fan and setting speed to 4\", \"Task1\": {\"Action\": \"on_fan1\", \"ActionValue\": \"4\"}}"
#     template=[{
#                 "role": "system",
#                 "content": instruction
#             }]
#     template.extend(text)
#     template.extend([{
#                     "role": "user",
#                     "content": query
#                 }])

#     return template
