# import os
# import wave
import json
import pyaudio
# import threading
from vosk import Model, KaldiRecognizer



def real_time_stt(stop_event):
    
    # Load the Vosk model
    model = Model("Models/vosk-model-en-in-0.5")

    # Initialize recognizer
    recognizer = KaldiRecognizer(model, 16000)

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Define callback function for audio stream
    def callback(in_data, frame_count, time_info, status):
        if stop_event.is_set():
            return (None, pyaudio.paComplete)  # Stop the stream
        
        if recognizer.AcceptWaveform(in_data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            text = result_dict['text']
            if len(text) > 5:
                with open("Transcript/transcript.txt", "a") as f:
                    f.write(" " + text)
            print(f"You said: {text}")
        else:
            partial_result = recognizer.PartialResult()
            partial_result_dict = json.loads(partial_result)
            # print(f"Partial: {partial_result_dict['partial']}")
        return in_data, pyaudio.paContinue

    # Start the audio stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=5000,
                    stream_callback=callback)

    print("Listening...")
    stream.start_stream()

    # Keep the program running
    try:
        while not stop_event.is_set():
            # pass
            stop_event.wait(timeout=0.1)
    except KeyboardInterrupt:
        stop_event.set()  # Graceful exit on Ctrl+C

    # Stop the stream and clean up
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Stopped listening.")



# Example usage
# if __name__ == "__main__":
#     real_time_stt()

