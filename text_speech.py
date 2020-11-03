import pyttsx3 as p 
# basics for converting text to speech 
# use pip install pyttsx3 

engine = p.init()
voices = engine.getProperty("voices") # to change the voice male to female
engine.setProperty("voice", voices[1].id)
volume =  engine.getProperty("volume") # to change voloume settings
print(volume)

engine.say("hello how are u doing?") # to convert to audio 
engine.runAndWait()

