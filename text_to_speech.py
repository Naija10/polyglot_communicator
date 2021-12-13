import cv2                                               #importing openCV library
import pytesseract                                       #optical character recognition (OCR) tool for python sponsored by google, to convert image to string
from PIL import Image                                    #adds image processing capabilities 
import googletrans                                       #importing the googletrans module
import os                                                #this module  provides functions for interacting with the  operating system
import gtts as gt                                        #google text to speech library
from googletrans import Translator,LANGUAGES

#IMAGE TO TEXT CONVERSION
#pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Naija\AppData\Local\Tesseract-OCR\tesseract"    # path where the tesseract module is installed 
img = Image.open('Data/india.jpeg')                               # opening an image from the source path 
result = pytesseract.image_to_string(img)                 #converts the image to  string  and  saves it to the result variable
print(result)                                             #prints the text which is in the image
#LANGUAGE CONVERSION
lang=list(LANGUAGES.values())                             #stores the list of languages supported in the lang variable              
print(lang)                                               #prints the languages                               
dest=input('enter the destination language:').lower()     #enter the destination language to which you to convert
if dest not in lang:
    print("Sorry! This language is not available ! Please try again")
else:
    translator=Translator()                                #creating an object named translator from the class Translator()
    desired_lan=translator.translate(result,dest)          #translating the given text to desird language using translate function
    res=desired_lan.text                                   #storing the translated text to res variable
    print(desired_lan.text)                                #prints the translated text
    print('pronunciation:',desired_lan.pronunciation)      #prints the pronunciation ofthetranslated text
#TEXT TO VOICE CONVERSION
lan=input('enter the language:').lower()                   # type gtts-cli --all to see the supported languages
speech=gt.gTTS(text=res,lang=lan)                          #converts the text to speech 
speech.save("output.mp3")                                  #saving the converted audio in  a mp3 file named output
os.system("start output.mp3")                              #playing the converted file
print("success")