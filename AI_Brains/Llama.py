import os
import json
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv
# from googlesearch import search
from Body import Internet_Data

load_dotenv() 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

date = datetime.now().date()
history_path = f"AI_Brains/History/{date}.txt"

def getHistory():
    # history_file = f"{history_path}{date}.txt"
    try:
        with open(history_path, "r") as file:
            return file.read()
    except FileNotFoundError: 
        return ""  

with open("AI_Brains/AI_System_Instructions.txt", "r") as f:
    instructions = f.read()

def Ask_LLM(query, SearchResult = None, AddToHistory = True):
    print(f"\n\033[93m>> Making Query request to LLM: '{query}'...\033[0m", end=" ")
    history = getHistory()
    if SearchResult != None:
        llama_query = f"""Previous Conversation: {history}\n```\n Search Results: {SearchResult}\n```\n Today's date: {str(date)}\n```\n Query: {query}"""
    else:
        # llama_query = "History: " + history + "\n``Today's date: "+ str(date)+"\nquery: " + query 
        llama_query = f"""Previous Conversation: {history}\n```\n Today's date: {str(date)}\n```\n Query: {query}"""


    client = Groq(api_key=GROQ_API_KEY)
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content":llama_query}
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ''.join(chunk.choices[0].delta.content or "" for chunk in completion)
    # print(f"String response: {response}")
    # Parse the JSON string
    parsed_json = json.loads(response)

    # if parsed_json.get("Task2", {}).get("Action") == "RealTimeData":
    #     AddToHistory = False

    # save the conversation to history file
    if AddToHistory:
        context = (
        f'{{"role":"user","content":"{query}"}}\n'
        f'{{"role":"model","content":{parsed_json}}},\n'
    )
        with open(history_path, "a") as file:
            file.write(context)
    print(f"Done.")
    print(f"\033[92m>>LLM: {parsed_json}\033[0m\n")
    return parsed_json



def get_llama(query):
    parsed_json = Ask_LLM(query, SearchResult = None, AddToHistory = True)
    
    task1 = parsed_json.get("Task1", {})
    task1_action = task1.get("Action")
    task1_action_value = task1.get("ActionValue")

    task2 = parsed_json.get("Task2", {})
    task2_action = task2.get("Action")
    task2_action_value = task2.get("ActionValue")


    if task2_action == "RealTimeData" and task2_action_value:
        print(f">> Collecting Data for: '{task2_action_value}'... ", end="")
        internet_data = Internet_Data.get_internet_data(task2_action_value)
        if internet_data:
            print(f"Done.\n>>>>Data: {internet_data}")
            return Ask_LLM(query=query, SearchResult=internet_data)
        else:
            print("Failed to get internet data.")
    return parsed_json