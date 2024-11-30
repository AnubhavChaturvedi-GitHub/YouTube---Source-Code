'''
✨ Support My Journey on YouTube! 🎥

Your support means the world to me as YouTube is one of my primary sources of income. By watching my videos, you’re helping me continue creating valuable content. Please take a moment to visit my channel and watch the video linked below all the way through—it makes a huge difference!

👉 Watch the Full Video Here! :- https://youtu.be/48vU7AAvxDo?si=e_NmfnQ2lk5jmYT7

Every view, like, and comment helps keep this dream alive. Thank you for being a part of my journey! 💖
'''

import os
import threading
import speech_recognition as sr # solve this error run 'pip install SpeechRecognition'

def recognize_speech():
    """
    This function captures audio in real-time and recognizes speech using Google Web Speech API.
    """
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Initializing microphone... Please wait.")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Microphone is ready! Start speaking.")

    def listen():
        while True:
            with mic as source:
                print("\nListening...")
                try:
                    audio = recognizer.listen(source, timeout=5)
                    print("Processing...")
                    # Recognize speech using Google Web Speech API
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                except sr.WaitTimeoutError:
                    print("No speech detected. Waiting for input...")
                except sr.UnknownValueError:
                    print("Sorry, could not understand the audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

    # Create a separate thread for real-time listening
    thread = threading.Thread(target=listen, daemon=True)
    thread.start()

    print("Press Ctrl+C to stop the program.")
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        print("\nProgram stopped by the user.")

if __name__ == "__main__":
    recognize_speech()
