import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer();
mic = sr.Microphone(device_index=0)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 178)



engine.setProperty('voice', 'english_rp+f4')
engine.say('Hello Zac')
engine.runAndWait()
engine.say('What can I do for you?')
engine.runAndWait()
try:
    with mic as source: 
        print('listening...')
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
   #     if ('snowy' and 'snow') in command:
        engine.say(command)
        engine.runAndWait()
        print(command)
except:
    pass

