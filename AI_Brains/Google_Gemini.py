import os
from dotenv import load_dotenv
import requests
import json

load_dotenv() 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
headers = {
    'Content-Type': 'application/json'
}

                
def Ask_Gemini(text, AI_NAME):
    Gemeni_prompt = "Imagine you are an AI named \""+AI_NAME+"\" that responds like a human. Keep responses brief and always in JSON format. Use the key \""+AI_NAME+"\" for your response, and if tasks are assigned, label them as \"Task1\", \"Task2\", and so on. Each task should include a sub-dictionary with \"Action\" for the task and \"ActionValue\" for its value. \nExample:\nUser command: \"turn on the fan1 and set the speed to 4\"\nYour response: { \""+AI_NAME+"\": \"Ok, turning on the fan and setting speed to 4\", \"Task1\": {\"Action\": \"on_fan1\", \"ActionValue\": \"4\"}}"
    data = {
        "contents": [
            # history
            {
                "role": "user",
                "parts": [
                    {
                        "text": text
                    }
                ]
            }
        ],
        "systemInstruction": {
            "role": "user",
            "parts": [
                {
                    "text": Gemeni_prompt
                }
            ]
        },
        "generationConfig": {
            "temperature": 0,
            "topK": 64,
            "topP": 0.95,
            "maxOutputTokens": 8192,
            "responseMimeType": "text/plain"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data)).json()


    text = response['candidates'][0]['content']['parts'][0]['text']

    # Remove the backticks and "json" to get the actual JSON string
    json_string = text.strip('```json\n').strip('```')

    # Parse the JSON string
    parsed_json = json.loads(json_string)

    # print(parsed_json)

    return parsed_json