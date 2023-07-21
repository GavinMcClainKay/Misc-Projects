import speech_recognition as speech
from gtts import gTTS
import openai

supported_languages = [
    'af', 'ar', 'bg', 'bn', 'bs', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 
    'et', 'fi', 'fr', 'gu', 'hi', 'hr', 'hu', 'id', 'is', 'it', 'iw', 'ja', 
    'jw', 'km', 'kn', 'ko', 'la', 'lv', 'ml', 'mr', 'ms', 'my', 'ne', 'nl', 
    'no', 'pl', 'pt', 'ro', 'ru', 'si', 'sk', 'sq', 'sr', 'su', 'sv', 'sw', 
    'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi', 'zh-CN', 'zh-TW', 'zh'
]

languages = [
    'Afrikaans', 'Arabic', 'Bulgarian', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Danish', 'German', 'Greek', 'English', 'Spanish',
    'Estonian', 'Finnish', 'French', 'Gujarati', 'Hindi', 'Croatian', 'Hungarian', 'Indonesian', 'Icelandic', 'Italian', 'Hebrew',
    'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Malayalam', 'Marathi', 'Malay', 'Myanmar (Burmese)',
    'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala', 'Slovak', 'Albanian', 'Serbian', 'Sundanese',
    'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai', 'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Chinese (Simplified)', 'Chinese (Mandarin/Taiwan)', 'Chinese (Mandarin)'
]

def GetApiKeyGPT(file) :
    api_key = open(file,'r').read()
    return api_key

def PromptGPT(prompt, model='gpt-3.5-turbo') :
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message['content']

def TranslateGPT(lang_tag, input) :
    openai.api_key = GetApiKeyGPT('./key/api_key.txt')
    language = languages[supported_languages.index(lang_tag)]
    return PromptGPT('Please translate the following into ' + language + ', be as accurate as possible to the meaning and intent of the text:\n' + input)
    
def SelectLanguage() :
    print('Supported Languages:\n')
    languages = open('Languages.txt', 'r').readlines()
    for language in languages :
        print(language)

    while(True) :
        selected_language = input('\nPlease select a language: ')
        if selected_language in supported_languages:
            return selected_language
        else :
            print('That is not a supported language, please try again.')

def GetInput() :
    recognizer = speech.Recognizer()
    try:
        with speech.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, 0.2)
            audio = recognizer.listen(source, timeout= 5)
            text = recognizer.recognize_google(audio).lower()
            return text
    except speech.RequestError as e:
        print('Could not request results; {0}'.format(e))
    except speech.UnknownValueError:
        print('unknown error occurred')
    exit()

def main() :
    language = SelectLanguage()
    print('Please begin')
    input = GetInput()
    output = TranslateGPT(language, input)
    tts = gTTS(text= output, lang= language, slow= False)
    tts.save("Output.mp3")


main()