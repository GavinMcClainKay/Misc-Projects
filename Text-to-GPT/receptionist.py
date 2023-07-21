# Python program to translate
# speech to text and text to speech
import pandas as pd
import openai
import time
import os
 
import speech_recognition as sr
import pyttsx3
 


# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
def GetApiKey(file):
    api_key = open(file,"r").read()
    return api_key

# Function to prompt GPT 3.5 turbo
def get_response(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


openai.api_key = GetApiKey("./key/api_key.txt")
recognizer = sr.Recognizer()

# Loop infinitely for user to speak
while(1):   
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            recognizer.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = recognizer.listen(source2)
             
            # Using google to recognize audio
            MyText = recognizer.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("##\t",MyText)
            prompt = MyText
            response = get_response(prompt)
            print("GPT\t", response)
            SpeakText(response)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")