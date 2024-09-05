import json
import pyaudio
from vosk import Model, KaldiRecognizer
import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 0.8
r.energy_threshold = 200
# r.dynamic_energy_threshold = True
# def real_time_stt(stop_event):

#     # Load the Vosk model
#     model = Model("Body/Models/vosk-model-en-us-0.22")

#     # Initialize recognizer
#     recognizer = KaldiRecognizer(model, 16000)

#     # Initialize PyAudio
#     p = pyaudio.PyAudio()

#     # Define callback function for audio stream
#     def callback(in_data, frame_count, time_info, status):
#         if stop_event.is_set():
#             return (None, pyaudio.paComplete)  # Stop the stream
        
#         if recognizer.AcceptWaveform(in_data):
#             result = recognizer.Result()
#             result_dict = json.loads(result)
#             text = result_dict['text']
#             if len(text) > 5:
#                 with open("Body/Transcript/transcript.txt", "a") as f:
#                     f.write(" " + text)
#             print(f"You said: {text}")
#         else:
#             partial_result = recognizer.PartialResult()
#             partial_result_dict = json.loads(partial_result)
#             # print(f"Partial: {partial_result_dict['partial']}")
#         return in_data, pyaudio.paContinue

#     # Start the audio stream
#     stream = p.open(format=pyaudio.paInt16,
#                     channels=1,
#                     rate=16000,
#                     input=True,
#                     frames_per_buffer=5000,
#                     stream_callback=callback)

#     print("Listening...")
#     stream.start_stream()

#     # Keep the program running
#     try:
#         while not stop_event.is_set():
#             # pass
#             stop_event.wait(timeout=0.1)
#     except KeyboardInterrupt:
#         stop_event.set()  # Graceful exit on Ctrl+C

#     # Stop the stream and clean up
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#     print("Stopped listening.")





def LiveSpeechToText(stop_event):
    print("LiveSpeechToText Listening...")
    while not stop_event.is_set():
        try:
            with sr.Microphone() as source:
                audio = r.listen(source,0,2)
            query  = r.recognize_google(audio,language='en-in')
            if query:  
                with open("Body/Transcript/transcript.txt", "a") as f:
                    f.write(" " + query)
                # return query
        except Exception as e:
            # pass
            print(e, end="")
            # return ""



def SpeechToText():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            audio = r.listen(source,0,4)
        query  = r.recognize_google(audio,language='en-in')
        return query if query else ""
    except Exception as e:
        # print(f"Error: {e}\n")
        return ""


