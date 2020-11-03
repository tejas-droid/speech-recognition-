import speech_recognition as sr
import pyttsx3 as p 

r = sr.Recognizer()
engine = p.init()

engine.say("hello how can i help you")

engine.runAndWait()


with sr.Microphone() as source:
    
    audio = r.listen(source)
    
    try:
        recognised_text = r.recognize_google(audio)
        print(recognised_text)
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError:
        print("error")
    engine.say("what do you want me to do")
    engine.runAndWait()