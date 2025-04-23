import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
#newsapi = # add our api key here

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com") 
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")  
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com") 
    elif "open linkdin" in c.lower():
        speak("opening linkdin")
        webbrowser.open("https://www.linkdin.com")  
    elif  c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link= musicLibrary.music[song]
       webbrowser.open(link)
    
if __name__ == "__main__":
    speak("Initializig Jarvis...")
    # Listning for the wake word "Jarvis"
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()


        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(audio)
            if (command.lower()== "jarvis"):
                speak("Helloo sir")
                #listen for command
                with sr.Microphone() as source:
                  print("Jarvis Active...")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)

                  processCommand(command)

                 
        except Exception as e:
            print("Error; {0}" .format(e))      
        
       
        
        
           



