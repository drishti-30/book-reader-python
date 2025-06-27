import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female

def speak(text):
    engine.say(text)
    engine.runAndWait()

file_name = r"C:\Users\drishti sharma\Documents\book.txt"

if os.path.isfile(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        speak("Reading your file now.")
        speak(content)
else:
    speak("File not found.")
