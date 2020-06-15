import keyboard
import speech_recognition as sr
import pyaudio
import sys
from pynput.keyboard import Key, Controller

r = sr.Recognizer()
typer = Controller()

def speech_to_text(all_chat=""):
	with sr.Microphone() as source:
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
		except:
			text = "Didn't work"
	if (text == 'quit'):
		sys.exit()
	typer.press(Key.enter)
	typer.release(Key.enter)
	typer.type("{}{}".format(all_chat,text))
	typer.press(Key.enter)
	typer.release(Key.enter)

while True:
	key_press = keyboard.read_key()
	if key_press == "9":
		speech_to_text("/all ")
	elif key_press == "8":
		speech_to_text()
	elif key_press == "3":
		sys.exit()
