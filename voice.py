import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndwait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am siri mam. Please tell me how may I hekp you")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!..")
        r.pause_threshold = 1
        audio = r.listen(source)
            
    try:
        print("Recognizing!..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
        elif 'open code' in query:
            codepath = " C:/Users/mamid/AppData/Local/Programs/Python/Python312/python.exe "
            os.startfile(codepath)