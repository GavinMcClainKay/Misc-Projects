#Gavin Kay 2023
#Program that randomly assigns 10 second break from study

import time
import random
import pyttsx3
import speech_recognition as sr

def InitTTS():
    tts = pyttsx3.init()
    tts.setProperty('voice', 2)
    return tts
#

def InitRecognizer():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source: 
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
    except:
        print("Speech Recognizer initialization failed. Ending Program")
        exit()

    return recognizer

def say(tts, output):
    tts.say(output)
    tts.runAndWait()
#

#in: speech recognizer instance from google speech_recognition
#out: lower case string of any speech recognized
def Listen(recognizer):
    command = ""
    #Voice input for string commands
    try:
        with sr.Microphone() as source: 
            audio2 = recognizer.listen(source)
            command = recognizer.recognize_google(audio2)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")

    command = command.lower()
    return command
#

#in: string command for program duration in minutes or hours
#out: duration for which to run the program in seconds
def ParseDuration(command):
    words = str.split(command, " ")
    amount = 0
    if(words[0].isdigit()):
        amount = int(words[0])
    else:
        return -1
    
    match words[1]:
        case "minutes":
            return 60 * amount
        case "hours":
            return 60 * 60 * amount
        case _:
            return -1
#

def Interupt(tts):
    say(tts, "Please take a 10 second silent break")
    time.sleep(10)
    say(tts, "Please resume study")
#

#in: pyttsx3 instance and duration in seconds
#out: none
def RandomlyInterupt(tts, duration):
    random.seed(time.time())

    #every 10 minutes I want to have 2 10 second breaks
    breaks = duration / 6000
    breaks = int(breaks)

    for i in range(breaks):
        first_break = random.randrange(1200, 3000)
        second_break = 6000 - first_break
        time.sleep(first_break)
        Interupt(tts)
        time.sleep(second_break)
        Interupt(tts)
#

tts = InitTTS()
say(tts, "Program Started, Please Wait a Moment")

recognizer = InitRecognizer()
say(tts, "How long would you like the study session to last, please specify minutes or hours.")

duration = 0
while(True):
    command = Listen(recognizer)
    duration = ParseDuration(command)

    if(duration == -1):
        say(tts, "Invalid input, please try again")
        continue

    else:
        say(tts, "Program will run for {}, press escape at any time to exit".format(command))
        break
#

RandomlyInterupt(tts, duration)
