import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Rajeev!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Rajeev!")   

    else:
        speak("Good Evening Rajeev!")   

    speak("I am Jarvis. Welcome Back. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source) #,timeout=8,phrase_time_limit=8

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com', 'PASSWORD OF MENTIONED ID')
    server.sendmail('xyz@gmail.com', to, content)
    server.close()

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
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Old jarvis\\Favourite songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Rajeev\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\Rajeev\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'email to test' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rk@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Rajeev. I am not able to send this email")
        
    speak("I am Jarvis. Welcome back. Please tell me how may i help you")

    
def takeCommand():    # It takes microphone input from the user and returns string output
    r = sr.Recognizer
    with sr.Microphone() as source:    # User will know that the programme is listening
        print("Listening...")
        r.pause_threshold = 1   # While speaking if the speaker takes gaps for 1sec then the code will not run
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"User said: {query}\n")   #query will be printed 
    
    except Exception as e:
#         print(e)      # It will print the error
        
        print("Say that again please...")
        return "None"
    return query
     
