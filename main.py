import pyttsx3
import datetime
import time
import webbrowser
import json
import requests

now= datetime.datetime.now()
current_time =now.strftime("%H:%M")
Today=datetime.date.today()
advice = requests.get("https://api.adviceslip.com/advice")
advice = advice.json()

#speak
engine =pyttsx3.init()
engine.setProperty('rate', 133)
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', 'english-us+f2')

def talk():
	ask =input('Hey There!, How can I help you?: ' ).lower()
	if "current time" in ask:
		engine.say("The current time is:", current_time)
		print(current_time)

	if "your name" in ask:
		engine.say('My name is EDITH')
		print('EDITH')

	if "what does edith mean?" in ask:
		print('EDITH stands for even dead im the hero')

	if "Which day is today?" in ask:
		print('Today is', Today)

	if ask in ['tell an advice' 'advice me' 'give an advice ']:
		print(advice['slip']['advice'])

	if "search google" in ask:
		url='https://www.google.com'
		webbrowser.get().open(url)



talk()
engine.runAndWait()
