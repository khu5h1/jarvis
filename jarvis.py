import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import os
import webbrowser
import pyjokes
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant,Pluto. What can i do for you, mam")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening, Please wait for a moment...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Analysing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Sorry, Please Say that again.")    
        print("Sorry, Please Say that again.")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")
            # webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif 'open instagram' in query:
            webbrowser.get('chrome').open("instagram.com")

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'open gmail' in query:
            webbrowser.get('chrome').open("gmail.com")

        elif 'open facebook' in query:
            webbrowser.get('chrome').open("facebook.com") 
        
        elif 'open gaana' in query:
            webbrowser.get('chrome').open("gaana.com") 
        
        elif 'open whatsapp web' in query:
            webbrowser.get('chrome').open("web.whatsapp.com") 
        
        elif 'open flipkart' in query:
            webbrowser.get('chrome').open("flipkart.com") 
       
        elif 'open amazon' in query:
            webbrowser.get('chrome').open("amazon.in") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'play music' in query:
            
            music_dir = 'music file address'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("The time is {strTime}")

        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you?") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 

        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me Jarvis") 
            print("My friends call me Jarvis") 

        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by Khu5h1") 
              
        elif 'joke' in query: 
            speak(pyjokes.get_joke())

        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 

     

        elif 'exit' in query: 
            speak("Okay, Thank You For Giving Me Your Time. Have a good day ahead.")
            exit(0)
