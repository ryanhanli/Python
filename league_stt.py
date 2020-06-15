import keyboard
import speech_recognition as sr
import pyaudio
import sys
from pynput.keyboard import Key, Controller

r = sr.Recognizer()
typer = Controller()

def speech_to_text():
	with sr.Microphone() as source:
		#print('Speak Anything : ')
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			#print('You said : {}'.format(text))
		except:
			text = "Didn't work"
			#print('Sorry could not recognize your voice')
	#keyboard.wait("9")
	if (text == 'quit'):
		sys.exit()
	typer.press(Key.enter)
	typer.release(Key.enter)
	typer.type(text)
	typer.press(Key.enter)
	typer.release(Key.enter)
	#print("You pressed 9")

while True:
	keyboard.wait("9")
	speech_to_text()
		

