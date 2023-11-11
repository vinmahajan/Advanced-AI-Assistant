#pip install Bardapi
from bardapi import BardCookies
import datetime
import os
import pyperclip
import pyautogui
import webbrowser
from time import sleep
import json
import datetime


today=datetime.date.today()
time=datetime.datetime.now().strftime("%H-%M-%S")


def CookieScrapper():
    print('scraping bard cookies...')
    webbrowser.open("https://bard.google.com/chat")
    sleep(3)
    try:
        sleep(3)
        notrobot = pyautogui.locateCenterOnScreen('pygui_screenshots/notrobot.png', confidence = 0.9)
        pyautogui.click(notrobot)
        pyautogui.sleep(3)
    except:
        pass
    extension = pyautogui.locateCenterOnScreen('pygui_screenshots/extension.png', confidence = 0.9)
    pyautogui.click(extension)
    # pyautogui.click(x=1733, y=70)
    pyautogui.sleep(1)
    etc = pyautogui.locateCenterOnScreen('pygui_screenshots/editthiscookie.png', confidence = 0.9)
    pyautogui.click(etc)
    # pyautogui.click(x=1479, y=247)
    pyautogui.sleep(2)
    ext = pyautogui.locateCenterOnScreen('pygui_screenshots/export.png', confidence = 0.9)
    pyautogui.click(ext)
    # pyautogui.click(x=1446, y=106)
    pyautogui.sleep(1)

    data = pyperclip.paste()
    pyautogui.hotkey('ctrl', 'w')

    try:
        json_data = json.loads(data)
        pass

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDValue = next((item for item in json_data if item["name"] == SID), None)
    TSValue = next((item for item in json_data if item["name"] == TS), None)
    CCValue = next((item for item in json_data if item["name"] == CC), None)

    if SIDValue is not None:
        SIDValue = SIDValue["value"]
    else:
        print(f"{SIDValue} not found in the JSON data.")

    if TSValue is not None:
        TSValue = TSValue["value"]
    else:
        print(f"{TSValue} not found in the JSON data.")

    if CCValue is not None:
        CCValue = CCValue["value"]
    else:
        print(f"{CCValue} not found in the JSON data.")

    cookie_dict = {
        "__Secure-1PSID": SIDValue ,
        "__Secure-1PSIDTS": TSValue,
        "__Secure-1PSIDCC": CCValue,
    }
    try:
        os.rmdir("cookies/bard_cookies")
        os.makedirs('cookies/bard_cookies')
    except:pass

    with open (f'cookies/bard_cookies/{today}.txt', 'w') as cookies:
        json.dump(cookie_dict, cookies)
    
    return cookie_dict


def Bard():

    while True:
        try:
            with open (f'cookies/bard_cookies/{today}.txt', 'r') as cookies:
                cookie_dict=json.load(cookies)
            if any(value is None for value in cookie_dict.values()) is True:
                raise(Exception)
        except:
            cookie_dict = CookieScrapper()

        cookie_exist=any(value is None for value in cookie_dict.values())

        if cookie_exist is False:
            print('Bard Initation Sucessful.')

            break
    try:
        bard = BardCookies(cookie_dict=cookie_dict)
    except:
        bard = BardCookies(cookie_dict=CookieScrapper())
        
    return bard


def get_reply(Query:str):
    Reply = Bard().get_answer(Query)['content'].replace('*', '')
    return Reply

def auto_execute():
    try:
        with open('AI_Brains\\cookies\\transcribe.txt', 'r') as transcribe:
            text=transcribe.read()

        with open('AI_Brains\cookies\HistoryCommand.txt', 'w') as HistoryCommand:
            History_command=HistoryCommand.read()

        if text and text != History_command:
            reply = get_reply(text)
            with open('AI_Brains\cookies\HistoryCommand.txt', 'w') as HistoryCommand:
                HistoryCommand.write(text)
        else:
            reply=None
        if reply:
            print(reply)
            data={'Time':time,"User":text,"AI":reply}
            with open(f'History/HistoryChat{today}.txt', 'a') as HistoryChat:
                HistoryChat.write(data)
            
        else:
            print('failed to get the reply')
    
    except Exception as e:
        print(e)