import pyttsx3  # pip install pyttsx3 == text 2 speech using python
import datetime
import speech_recognition as sr
import smtplib
from secrets import sendermail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices():
    voices = engine.getProperty('voices')
    print(voices[0].id)


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is:")
    speak(Time)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning mr.sumra!")
    elif hour >= 12 and hour < 16:
        speak("good afternoon sir ")
    elif hour >= 16 and hour < 19:
        speak("good evening sir, it's time for cycling!")
    else:
        speak("good night tofik,have a peaceful sleep")

def tofik():
    speak("hello this is Friday! created by mr.taufik sumra")

def wishme():
    speak("friday in your service, i'm here to assist you, all things are normal have a good day sir")
    greeting()
    
def takeCommandMic():
    query = input("please tell me how can i help you?\n")
    return query


def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.51
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please....")
        return "None"
    return query


def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sendermail, epwd)
    email = EmailMessage()
    email['From'] = sendermail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


def sendwhatsmessage(phone_no, message):
    message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
    sleep(10)
    pyautogui.press('enter')


def searchgoogle():
    speak('what should i search for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)


def news():
    newsapi = NewsApiClient(api_key='2fbcf1b82c154112ac55ff1dccb866ca')

    data = newsapi.get_top_headlines(q='fast and furious 9',
                                     language='en',
                                     page_size=5)

    newsdata = data['articles']
    for x, y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

    speak("that's it for now i'll update you in sometime")


def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered :{data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'E:\\computer\\jarvis 2.0\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+ usage)
    battery = psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)


if __name__ == "__main__":
    tofik()
    # wishme()
    while True:
        query = takeCommandMic().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'email' in query:
            email_list = {
                'test email': 'jb64549857@gmail.com'
            }
            try:
                speak("To whom you want to send the mail?")
                name = takeCommandMic()
                receiver = email_list[name]
                speak('what is the subject of the mail?')
                subject = takeCommandMic()
                speak('what should i say?')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("unable to send the email")

        elif 'message' in query:
            user_name = {

                'Friday': '+91 58xxxxx65'
            }
            try:
                speak("To whom you want to send the whats app message?")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak('what is the message?')
                message = takeCommandMic()
                sendwhatsmessage(phone_no, message)
                speak("message has been send")
            except Exception as e:
                print(e)
                speak("unable to send the message")

        elif 'wikipedia' in query:
            speak('searching on wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'search' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak('what should i search on yoooutube?')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)

        elif 'weather' in query:
            city = 'kheralu'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=aa707a0e04cc13753dae5361d29e07ee'

            res = requests.get(url)
            data = res.json()

            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            desp = data['weather'][0]['description']
            temp = round((temp - 32) * 5/9)
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} city is like')
            speak('temperature : {} degree celcius'.format(temp))
            speak('weather is {}'.format(desp))

        elif 'news' in query:
            news()

        elif 'read' in query:
            text2speech()

        elif 'covid' in query:
            covid()

        elif 'code' in query:
            codepath = 'C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(codepath)

        elif 'atom' in query:
            atompath = 'C:\\Users\\LENOVO\\AppData\\Local\\atom\\atom.exe'
            os.startfile(atompath)

        elif 'open' in query:
            os.system('explorer c://{}'.format(query.replace('open','')))

        elif 'open' in query:
            os.system('explorer f://{}'.format(query.replace('open','')))

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'screenshot' in query:
            screenshot()

        elif 'password ' in query:
            passwordgen()

        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommandMic()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that"+remember.read())

        elif 'cpu' in query:
            cpu()

        elif 'logout ' in query:
            os.system("shutdown -1")

        elif 'shutdown ' in query:
            os.system("shutdown /s /t 1")

        elif 'restart ' in query:
            os.system("shutdown /r /t 1")
            
        elif 'offline' in query:
            quit(speak("Ok sir, Take Care."))
            
