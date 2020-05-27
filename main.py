import speech_recognition as sr 
import pyttsx3
import datetime
import time
import webbrowser
from playsound import playsound

now= datetime.datetime.now()
current_time =now.strftime("%H:%M")
current_time = str(current_time)
Today=datetime.date.today()

class person:
	name = ''
	def setName(self,name):
		self.name=name

def there_exist(terms):
	for term in terms:
		if term in text:
			return True


def speak(tts):
	engine =pyttsx3.init()
	engine.setProperty('rate', 150)
	engine.say(tts)
	engine.runAndWait()

r =sr.Recognizer()
def listen():
	with sr.Microphone() as source:

		audio= r.listen(source)
		text = ''

		try:
			text = r.recognize_google(audio)
		except sr.UnknownValueError:
			speak('Sorry, I did not get that')
		except sr.RequestError:
			speak('Sorry, It seems you have connection issues. Check your internet connection')
		return text.lower()

speak('Hello there, How can I help you?')
print('How can I help You')

text = listen()

def response(audio_file):
	#Greeting
	if there_exist(['Hi', 'Hello', 'Hey Edith', 'Edith']) :
		speak("Hey there")


	#save user name
	if there_exist(["my name is"]):
		person_name = text.split("is")[-1].strip()
		speak(f"Ok i will rember that {person_name}")
		character.setName(person_name)
	#Time 
	if there_exist(['current time', 'what is the time', 'what is the current time']):
		speak('The current time is '+ current_time)

	#name
	
	try:
		if there_exist(['my name', 'what is my name', 'who am i']):
			speak(f'Your name is {person_name}')
	except UnboundLocalError:
		speak('I dont know yet who you are, who do you want me to call you?')
		person_name = text.split('me') [-1].strip()
		character.setName(person_name)
		if there_exist(['call me']):
			speak(f'okey i will remember that {person_name}')


	if there_exist(['your name', 'who are you', 'how can i call you?', 'what is your name']):
		speak('Im EDITH, Your personal assistant')


	#Day
	if there_exist(['which day is today', 'when is today', 'today']):
		speak('today is' +Today)
	
	#search google
	if there_exist (['search for']) and 'youtube' not in text:
		search_term = text.split('for')[-1]
		url = f"https://www.google.com/search?q={search_term}"
		webbrowser.get().open(url)
		speak(f"Here is what i found on {search_term} ")

	if there_exist(['youtube']):
		search_term =text.split('for')[-1]
		url =f"https://www.youtube.com/results?search_query={search_term}"
		webbrowser.get().open(url)
		speak(f"Here is what i found on {search_term} in youtube")


	if there_exist(['quit', 'exit', 'leave', 'bye' ,'good bye']):
		speak('Bye, See you when you need my help')
		exit()

time.sleep(1)

character =person()

while (1):
	text = listen()
	response(text)