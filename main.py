import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
from gtts import gTTS
recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    

    # Initialize the mixer
    pygame.mixer.init()

    # Load and play the MP3 file
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    # Keep the program running until the music finishes
    while pygame.mixer.music.get_busy():
       pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


news_API_KEY="your news api key"

def geminiProcess(command):
    # Set the API endpoint and your API key
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=your gemini api key'
    headers = {
    'Content-Type': 'application/json',
    }
    data = {
    "contents": [
        {
            "parts": [
                {
                    "text": command
                }
            ]
        }
    ]
    }

    # Send the POST request
    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    # Check if 'candidates' key exists in the response
    if 'candidates' in result:

        # Extract the answer, remove newlines, and make sure it's in one line
        answer = " ".join(result['candidates'][0]['content']['parts'][0]['text'].split())
        # Extract the token count
        token_count = result['usageMetadata']['totalTokenCount']
    else:
       print(f"Error: 'candidates' key not found in the response. Full response: {result}")
    
    return answer

def processCommand(c):
    if("open google" in c.lower()):
        webbrowser.open("https://google.com")
    elif("open facebook" in c.lower()):
        webbrowser.open("https://facebook.com")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://youtube.com")
    elif(c.lower().startswith("play")):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={news_API_KEY}")
        if r.status_code==200:
            #Parse the json response 
            data=r.json()
            #Extract the articles 
            articles=data.get('articles',[])
            #Print the headlines
            for article in articles:
                speak(article['title'])


    else:
        #lets gemini handle else request:
        output=geminiProcess(c)
        speak(output)

if __name__=="__main__":
    speak("Initialising Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()

        
        
        # recognize speech using Jarvis
        try:
            with sr.Microphone() as source:
                print("Listening...")
                #listen for the wake word "Jarvis"
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            print("Recognizing.....") 
            word=r.recognize_google(audio)
            if(word.lower()=='jarvis'):
                speak("Ya")
                #listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                command=r.recognize_google(audio)
                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
