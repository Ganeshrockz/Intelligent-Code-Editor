import telepot
import speech_recognition as sr
import requests
import subprocess
import os
import time
import parseInput

token='558301122:AAE4rEvHQYhJtnw1EM0_SKPa5lb1ctVf_O8'

bot=telepot.Bot(token)

chatId=183429563
def voiceInputHandler(msg):
	r = sr.Recognizer()
	voiceFileId = msg['voice']['file_id']
	audioFile = bot.getFile(voiceFileId)
	print(audioFile['file_path'])
	fileReceiveStatus = requests.get("https://api.telegram.org/file/bot"+ str(token) + "/" + str(audioFile['file_path']))
	audioFilePath = audioFile['file_path']
	fi = open('file.oga','wb')
	fi.write(fileReceiveStatus.content)
	fi.close()
	srcFileName = 'file.oga'
	destFileName = 'file.wav'
	try:
		subprocess.call('ffmpeg -i %s %s' %(srcFileName,destFileName) , shell = True)
		time.sleep(5)
	except:
		print("Subprocess Error")
	audioFile = sr.AudioFile('file.wav')
	with audioFile as source:
		audio = r.record(source)
	os.remove('file.oga')
	os.remove('file.wav')
	try:
		recogText = r.recognize_google(audio)
	except:
		bot.sendMessage(chatId,"Sorry!!! Speak again")
		return ""
	bot.sendMessage( chatId , "The spoken text is "+ '"' +str(recogText)+ '"')
	print(recogText)
	return recogText
def handle(msg):
	msgText=""
	try:
		if(msg['voice']):
			msgText = voiceInputHandler(msg)
			if( msgText == ""):
				return
			msgText = msgText.lower()
			parseInput.inputParseText(msgText)
	except:
		msgText = msg['text']

bot.message_loop(handle, run_forever = 'Running ...')