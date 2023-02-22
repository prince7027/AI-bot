import speech_recognition as sr 
import playsound  
import random
from gtts import gTTS  
import ssl
import webbrowser
import certifi
import time
import os  # remove the audio files
import subprocess
import pyttsx3
from PIL import Image
import pyautogui  # Screenshot
import bs4 as bs
import urllib.request
from pyttsx3 import engine


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in value_date:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()  # initialise the recognizer


# listen for audio and convert it to text

def record_audio(ask=""):
    with sr_Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = ask.listen(source, 5, 5)  # listen for audio via source
        print("Done listening")
        voice_data = ""
        try:
            voice_data = r.recorginize_google(audio)  # convert audio to text
        except sr.UnknownValueError:
            engine_speak("Sorry , I did not get that")
        except sr.RequestError:
            engine_speak("Sorry server is down")
            print(">>", voice_data.lower())  # print what the  user said
            return voice_data.lower()


def engine_speak(audio_string):
    audio_string = srt(audio_string)
    tts = gTTS(text=audio_string, lang="en")  # text to speech
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # help u sto play the audio
    print(asis_obj.name + ":", audio_string)  # print what app said
    os.remove(audio_file)


def reponf(voice_data):
    # greeting
    if there_exists(['hello', 'hi', 'hey', 'meow', 'hola']):
        greetings = ['hey,how can i help you' + person_obj.name, 'how can i help you'
                     + person_obj.name, 'hello' + person_obj.name]

        greet = gretings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    # name

    if there_exists(['what is your name', 'tell me your name']):
        if person_obj.name:
            engine_speak(
                "i dont know my name ,please give my name by saving command your anme should be,,,, what is your name")
        else:
            engie_speak("what is your name ")

    if there_exists(["my name is"]):
        person_name = voice_data.split('is')[-1].strip()
        engine_speak("okay i'll remember that your name is " + person_name())
        person_obj.setName(person_name)  # remember name in person object

    if there_exists(['your anme should be ']):
        asis_name = voice_data.split('be')[-1].strip()
        engine_speak('okay ill remember that your name is ' + asis_name())
        person_obj.setName(person_name)  # remember name in asis object

        # greeting

        if there_exists(["how are you", "how are you doing"]):
            engine_speak("i'm very well thanks for asking" + person_obj.name)

        # time
        if there_exists(["what's the time", "tell me time"]):
            time = ctime().split(" ")[3].split(":")[0:2]

            if time[0] == '00':
                hours = '12'

            else:
                hours = time[0]
                minutes = time[1]
                time = hours + 'hours and' + minutes + 'minutes'
                engine_speak(time)

            # toss a coin

            if there_exists(['flip a coin', 'toss a coin']):
                moves = ['head', 'tails']
                cmove = random.choice(moves)
                engine_speak('you got' + cmove)

            # search google

            if there_exists(['search for']) and 'youtube' not in voice_data:
                search_term = voice_data.split("for")[-1]
                url = 'https://google.com/search?q' + search_term
                webbrowser.get().open(url)
                engine_speak('I found something about' + search_term + 'on google')

            # search youtube

            if there_exists(['youtube']):
                search_term = voice_data.split('for')[-1]
                url = 'https://www.youtube.com' + search_term
                webbrowser.get().open(url)
                engine_speak('done')

            # game

            if there_exists(['lets play rock, paper and scissor']):
                voice_data = record_audio('choose among rock,paper and scissor')
                moves = ['rock', 'paper', 'scissor']
                cmove = random.choice(moves)
                pmove = voice_data
                engine_speak('I am choose' + cmove)

                # exit
                if there_exists(['out', 'exit', 'bye']):
                    engine_speak('Ok')
                    exit()

                if pmove == cmove:
                    engine_speak('match is draw lets play one more time')
                elif pmove == 'rock' and cmove == 'scissor':
                    engine_speak('Congratulations you win')
                elif pmove == 'rock' and cmove == 'paper':
                    engine_speak('You loose')
                elif pmove == 'scissor' and cmove == 'paper':
                    engine_speak('Congratulations you win')
                elif pmove == 'scissor' and cmove == 'rock':
                    engine_speak('You loose')
                elif pmove == 'paper' and cmove == 'rock':
                    engine_speak('Congratulations you win')
                elif pmove == 'paper' and cmove == 'scissor':
                    engine_speak('You loose')
    time.sleep(1)
    asis_obj = asis()
    person_obj = person()
    asis_obj.name = 'Phoenix'
    engine = pyttsx3.init()

    while (1):
        voice_data = record_audio('Recording')  # get the sound input
        print('Done')
        print("Initialize:..." + voice_data)
        respond(voice_data)  # responce
        # wikipidia
