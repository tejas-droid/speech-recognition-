import speech_recognition as sr
import datetime
import pyttsx3 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
# install seleium pip install selenium
import time #import time 



engine = pyttsx3.init()
voices = engine.getProperty('voices')
#voices is a list of voices on your computer
engine.setProperty('voice',voices[1].id)
driver = webdriver.Chrome(executable_path = "E:\\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)
def youtube(name):
	driver.get("https://www.youtube.com/results?search_query="+ name)

	driver.find_element_by_xpath('//*[@id="dismissable"]').click()

	time.sleep(3)
	#duration = driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div > span.ytp-time-duration')
	duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
	#print(duration)
	#print(duration.text[-2:])
	time.sleep(int(duration.text[-2:])+6)
	duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
	#print(duration)

	c = duration.text
	mins  = int(c[:1])
	sec = int(c[-2:])
	total_time = (mins*60) + sec
	#print(total_time)

	time.sleep(total_time + 5)

	driver.close()
    
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	
	if hour>=0 and hour<12:
		speak("good morning Sir")

	elif hour>=12 and hour<18:
		speak("good afternoon sir")
	
	else:
		speak("Good Evening sir")

	speak("I am jarvis sir. Tell me how can i help you?")

def takeCommand():
	#it takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		
	try:
		print("Recognizing...")
		query = r.recognize_google(audio,language='en-in')
		#print(f"User said; {query}\n")

	except Exception as e:
		print(e)
		print("Say That Again Please...")
		return "None"

	return query
wishMe()
print(youtube(takeCommand()))
