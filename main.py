#importing necessary modules
import cv2                                               #importing openCV library
import pytesseract                                       #optical character recognition (OCR) tool for python sponsored by google, to convert image to string
from PIL import Image                                    #adds image processing capabilities 
import googletrans                                       #importing the googletrans module
import os                                                #this module  provides functions for interacting with the  operating system
import gtts as gt          								 #google text to speech library
from googletrans import Translator,LANGUAGES  			 #importing languages from googletrans
from configparser import ConfigParser					 #for accessing inputs via config.ini file
from typing import Tuple

class TextToSpeech:
	'''Converting the taken input image into desired language and as a voice too''' 


	def __init__(self, input_image: str) -> None:
		'''
		Constructor of class TextToSpeech
		Arguments:
			input_image: fetching the input image from the system
		Returns:
			None
		'''
		self.input_image = input_image

	def image_to_text(self) -> str: 
		'''
		Converts the image to string
		Returns:
			text: the recognized text from the given input image using pytesseract
		'''
		img = Image.open(self.input_image)
		text = pytesseract.image_to_string(img)
		print("Recognizing words in the given image----> ")
		return text

	def translation(self, text: str)-> Tuple[str, str]:
		'''
		Prints the languages and converts the text to destination lang which we want
		Parameters:
			text: the recognized text from the given input image using pytesseract
		Returns:
			translated_text: text which is translated to the desired language
			pronounciation_text: the correct pronounciation of the translated language
	    '''
		self.text = text
		lang=list(LANGUAGES.values())
		print(lang) 
		dest=input('Enter the destination language to translate:').lower()
		if dest not in lang:
   			print("Sorry! This language is not available ! Please try again")
		else:
			translator=Translator()
			desired_lan=translator.translate(self.text, dest)
			translated_text = desired_lan.text
			pronunciation_text = desired_lan.pronunciation
		return translated_text, pronunciation_text

	def text_to_voice(self, translated_text: str)-> None:
		'''
    	Converts the text to speech and save the converted audio in a mp3 file format
    	Parameters:
    		translated_text: text which is translated to the desired language
    	Returns:
    			None
    	'''
		speech_lan = input('Enter the language (for speech conversion):').lower()
    	#type gtts-cli --all in command prompt to see the supported languages
		speech=gt.gTTS(text = translated_text, lang = speech_lan)
		speech.save("output.mp3")
    	#os.system("start output.mp3")
    	

if __name__ == '__main__':

	#main code 
    config = ConfigParser()
    config.read("config.ini")
    print("Starting the text to speech conversion")

    #fetching input image
    input_image = config['input_image']['image']
    polyglot = TextToSpeech(input_image)

    #Recognizing the text and translates to the desired language
    text = polyglot.image_to_text()
    print(text)
    translated_text, pronunciation_text = polyglot.translation(text)
    print("Translated text:\n")
    print(translated_text)
    #print('pronunciation:\n',pronunciation_text)

    #Translated text to speech
    speech = polyglot.text_to_voice(translated_text)
    print("successfully converted")
	