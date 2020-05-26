import pyttsx3
engine =pyttsx3.init()

voices =engine.getProperty('voices')
for voice in voices:
    print("voice:")
    print("-ID: %s" % voice.name)
    print("- Name: %s" % voice.languages)
    print("- Gender: %s" % voice.gender)
    print("-Age: %s" % voice.age)
