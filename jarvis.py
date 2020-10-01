import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')  # to use the voice provided by windows
voices = engine.getProperty('voices')  # To get the list of voices
engine.setProperty('voices', voices[0].id)  # to select the voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your assistant sir!!! How may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query
def runCommand():
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, Sentences=2)
            speak("According to Wiki")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'play music' in query:
            music_dir = 'C:\\Khushi\\Songs\\MyFavorites'
			songs = os.listdir(music_dir)
			os.startfile(os.path.join(music_dir, songs[0]))

if __name__ == "__main__":
    wishMe()
    takeCommand()
    runCommand()
    
    # executing tasks
