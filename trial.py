import pyttsx3 as psp
import datetime as date
import speech_recognition as sp
import webbrowser as web
import wikipedia 

engine=psp.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    t=sp.Recognizer()
    with sp.Microphone() as sources:
        print("Listening....")
        t.pause_threshold=1
        audio=t.listen(sources)
        try:
            print("Reccognising....")
            query=t.recognize_google(audio,language="en-in")
            print(f"user said {query}\n")
        except Exception as e:
            print("Say that again please")
            return "None"
        return query

def wishme():
    hour=int(date.datetime.now().hour)
    if(hour>12 and hour<17):
        speak("Good afternoon")
    elif(hour<12 and hour<0):
        speak("Good Morning")
    elif(hour>17 and hour<20):
        speak("Good Evening")
    elif(hour>20 and hour<24):
        speak("Good night")

if __name__ == "__main__":
    speak("Hii sneha")
    wishme()
    speak("How can I help you?")
    takecommand()
    while True:
        query=input("please enter the command  ")
        query=takecommand().lower()
        if ("open youtube" in query ):   
            web.open("www.youtube.com")
        elif "open wikipedia" in query:
            speak("searching file")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=5)
            speak("According to wikipedia:")
            print(result)
            speak(result)
