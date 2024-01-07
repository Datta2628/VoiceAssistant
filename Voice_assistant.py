import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Your Voice Assistant. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code of numpy' in query:
            codePath = r"C:\\Users\\yadav\\Documents\\Python\\Numpy.exe"
            os.startfile(codePath)

        elif 'open mail' in query:
            mail_url = "https://mail.google.com"  # Replace with the URL of your email provider
            webbrowser.open(mail_url)
            speak("Opening your mail in the browser")

        elif 'open teams' in query:
            teams_url = "https://teams.microsoft.com"
            webbrowser.open(teams_url)
            speak("Opening Microsoft Teams")

        elif 'open eviden' in query:
            eviden_url = "https://www.eviden.com"
            webbrowser.open(eviden_url)
            speak("Opening Eviden.com")

        elif 'open atos location' in query:
            pune_atos_url = "https://www.example.com/pune/atos-location"
            webbrowser.open(pune_atos_url)
            speak("Opening Pune Atos Location")
