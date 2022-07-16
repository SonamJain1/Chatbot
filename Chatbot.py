import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import time
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices)

#voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"   # female voice 
engine.setProperty('voice',voices[0].id)
#engine.setProperty('voice',voices[1].id) # for femail voice
engine.say('i m back for u sir ')
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning sir')
    elif hour>=12 and hour<16:
        speak('good afternoon sir')
    elif hour>=16 and hour<=20:
        speak('good evening sir')
    else:
        speak('good night sir ')
    speak('i am jarvis sir. please tell me how may i help you')

def takecommand(): # take command to microphone from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listing.......')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print('recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f"user say : {query}\n")
    except Exception:
        print('please say again...')
        return 'none'
    return query


if __name__ == "__main__":
    speak('my boss name is hirdesh')
    wishme()
    while True:
#    if 1:
        query = takecommand().lower()         # logic for exquting task
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(result)
            speak(result)       

        elif 'open youtube' in query:
            webbrowser.open('youTube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'facebook' in query:
            webbrowser.open('facebook.com')

        elif 'instagram' in query:
            webbrowser.open('instagram.com')

        elif 'whatsapp web scan' in query:
            webbrowser.open(r'https://web.whatsapp.com/')

        elif 'play music' in query:
            music_dir = 'F:\\DC Downloads\\Music Peace'
            songs = os.listdir(music_dir)
           # print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
        #    strTime = time.asctime()

            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'quit' in query:
            exit()

        elif 'video' in query:
            videopath = "E:\\jarvis"
            os.startfile(os.path.join(videopath))
