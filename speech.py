import pyttsx3

engine =pyttsx3.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', 'english-us+f1')
engine.say('hello world!')
engine.runAndWait()
