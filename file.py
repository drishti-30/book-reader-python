import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Welcome! This is your book reader.")

# CORRECT path to your file
file_name = r"C:\Users\drishti sharma\Documents\book.txt"

if os.path.isfile(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        speak("Reading the book now.")
        speak(content)
else:
    speak("Sorry, file not found. Please check the file name.")
