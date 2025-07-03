import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<16:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hello Madam I am Jarvis. Please Tell me how can I help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please")
        return "none"
    return query

if __name__=="__main__":
    wishMe()
    if 1:
      query=takeCommand().lower()
      if 'wikipedia' in query:
        speak('Searching Wikipedia.....Please Wait')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
      elif 'open youtube' in query:
        speak('opening youtube')
        webbrowser.open('youtube.com')
      elif 'open google' in query:
        speak("opening google")
        webbrowser.open('google.com')
      elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'Madam the Time is{strTime}')
      elif 'open code' in query:
        speak("opening visual studio code")
        codePath="D:\\Microsoft VS Code\\Code.exe" 
        os.startfile(codePath)
      elif 'who are you' in query:
        speak("My Dear. I am Jarvis the best Artificial intelligence in the world")
      elif ' my name' in query:
        speak('Your name is Devraj')
      elif 'are you from' in query:
        speak("I am From stark tower")
      elif 'me about you' in query:
        speak("I am Jarvis my coding address is stark tower . i am an artificial intelligence  .i am here to help you ")
      elif 'about me'in query:
        speak('hello girl you are very beautiful and young girl of age 17  ')
      elif'about my mother'in query:
        speak("Hi Manju singh you are a great mom in the world,and a great wife,and great women")
      

      
        
