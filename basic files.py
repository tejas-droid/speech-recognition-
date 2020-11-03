import speech_recognition as sr

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("welcome")
    audio = r3.listen(source)
print(r2.recognize_google(audio))