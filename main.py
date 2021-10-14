import speech_recognition as sr
from time import ctime
import webbrowser as wb
import time


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry,I did not heard you')
        except sr.RequestError:
            print('Sorry,my speech service is down')
        return voice


def respond(voice):
    if 'what is your name' in voice:
        print('My Name is Alexa')
    if 'what time is it' in voice:
        print(ctime())
    if 'search' in voice:
        search = record_audio('what do you want to search?')
        url = 'https://google.com/search?q=' + search
        wb.get().open(url)
        print('here what i found' + search)
    if 'find location' in voice:
        location = record_audio('what is the location?')
        url = 'https://www.google.co.in/maps/place/' + location + '/&amp;'
        wb.get().open(url)
        print('here what i found' + location)
    if 'open' in voice:
        youtube = record_audio('what you want to find on you tube ?')
        url = 'https://www.youtube.com/' + youtube
        wb.get().open(url)
        print('here what i found' + youtube)
    if 'exit' in voice:
        exit()


time.sleep(1)
print('How Can I help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)
