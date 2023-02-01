# -------------------------------PBL PROJECT-------------------------------------------
# TOPIC: ------DESKTOP ASSISTANCE USING PYTHON PROGRAMMING------'Yudhishthir'--------

# PRESENTED BY: TEAM :------------- PANDAV --------------------------------------------
# 1) PRASAD UNECHA
# 2) YASH KULKARNI
#---------------------------------LET'S BEGIN------------------------------------------

                                                            #'All COMMENTS'
from __future__ import print_function
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from time import ctime
from tkinter import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
                                                           # print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
                                                           # getting details of current speaking rate
    rate = engine.getProperty('rate')
                                                           # printing current voice rate
                                                           # setting up new voice rate
    engine.setProperty('rate', 150)


def wishMe():                                              # 'WHISH ME FUNTION'
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    speak(" my name is yudhishthir. hello Friend , how may i help you?")
    


def takeCommand(ask=False):
                                                           # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            print(ask)
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)

    except Exception as e:
                                                                     # print(e)

        print("say that again please....")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while (True):
        query = takeCommand().lower()

        if 'wikipedia' in query:                                   # Wikipedia search 
            speak('searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'time' in query:                                      # speaks the time
            print(ctime())
            speak(str('time is'+ ctime()))           

        elif 'how are you' in query:
            speak('I AM FINE BOSS, HOW ARE YOU?')

        elif 'fine' in query:
            speak('nice to hear about it boss')

        elif 'rest' in query:
            speak('Thank You boss ,will meet you soon')

        elif 'youtube' in query:
            speak('opening youtube.')
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak('opening google')
            webbrowser.open("google.com")

        elif 'introduce' in query:                                # yudhishthir introduction
            speak('A WARM  WELCOME TO  EVERYONE PRESENT HERE. MY NAME IS YUDHISHTHIR . I AM YOUR VIRTUAL DESKTOP ASSISTANT. I HAVE BEEN CREATED BY A GROUP OF EXTRAORDINARY STUDENTS OF PUNE INSTITUTE OF COMPUTER TECHNOLOGY .   MY NAME  GETS ITS ROOTS FROM INDIAN MYTHOLOGY. THE NAME YUDHISHTHIR REFERS TO THE ELDEST SON OF KING PAANDU AND HIS WIFE , THAT IS QUEEN KUNTI. THE MAIN MOTIVE OF MY CREATION IS TO ANSWER PEOPLE WHO ASK FOR HELP.  WITH THE HELPP OF MY CREATORS I AM CONSTANTLY EVOLVING AND THIS EVOLUTION SEEMS TO HAVE NO END. THANK YOU EVERYONE AND I HOPE YOU WILL BE SATISFIED WITH MY SERVICE')

        elif 'teacher' in query:                                  
            speak('Sure , it will be by honor. The chief guest for today is DOCTOR  USHA POLINA . USHA MAM has completed her graduation in B S C in maths,  Physics , chemistry.  Along with this MADAM has completed her masters in M S C , PHYSICS. She has completed her doctorate in PHYSICS.  MAM has an Area of specialisation in SOLAR cells that is a part of  Solar state Physics.BUT this is not over yet . DOCTOR usha polina didn’t just stop at this . she pursued her career in the field of teaching. Over 8 years of Experience in teaching mam is a faculty of physics at one of the most reputed engineering college in Maharashtra . that is Pune institute of computer technology. She also has 5 international journals in her name. My creation was possible due to MAM’s guidance.  I will like to conclude by thanking mam in helping and guiding students and wish  you will do the same in the future.')

        elif 'certificate' in query:                              # certificate generator
            from os import close
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.base import MIMEBase
            from email import encoders
            import csv
            from PIL import Image, ImageDraw, ImageFont
            import pandas as pd



            df = pd.read_csv('data.csv')                          # data csv file
            font = ImageFont.truetype('arial.ttf', 60)
            for index, j in df.iterrows():
                img = Image.open('image.jpeg')
                draw = ImageDraw.Draw(img)
                draw.text(xy=(371, 334), text='{}'.format(
                    j['name']), fill=(0, 0, 0), font=font)
                img.save('pictures/{}.jpeg'.format(j['name']))

            mail_content = '''We congratulate you on your grand success in the National Cricket Championship. 
                        Please find your Certificate of appreciation attached below.

                                    Thank You
            '''
                                                                  # The mail addresses and password
            sender_address = 'yudhishthirpbl@gmail.com'
            sender_pass = 'firstpandav'
            with open('data.csv', encoding='utf-8') as file:
                reader = csv.reader(file)
                emails = []
                names = []

                for row in reader:
                    emails.append(row[1])
                    names.append(row[0])
            del emails[0]
            del names[0]
            print(emails)
            print(names)
            receiver_address = ''
                                                                  # Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Congratulations'
                                                                  # The subject line
                                                                  # The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
                                                                  # Create SMTP session for sending the mail
                                                                  # use gmail with port
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()                                    # enable security
                                                                  # login with mail_id and password
            session.login(sender_address, sender_pass)
            text = message.as_string()
            for i in range(len(names)):
                attach_file_name = 'pictures/' + names[i] + '.jpeg'
                                                                  # Open the file as binary mode
                attach_file = open(attach_file_name, 'rb')
                payload = MIMEBase('image', 'jpeg')
                payload.set_payload((attach_file).read())
                                                                  # encode the attachment
                encoders.encode_base64(payload)
                                                                  # add payload header with filename
                payload.add_header('Content-Decomposition',
                                   'attachment', filename=attach_file_name)
                message.attach(payload)
                                                                  # login with mail_id and password
                session.login(sender_address, sender_pass)
                text = message.as_string()
                session.sendmail(sender_address, emails[i], text)
                payload.set_payload((attach_file).close())
                attach_file_name = ''
            session.quit()
            print('Mail Sent')
            speak('certificate send to mail')
            
        elif 'calculator' in query:                               # custom build calculator by assistance
            speak('opening calculator')

            def click(event):
                global scvalue
                text = event.widget.cget("text")
                print(text)
                if text == "=":
                    if scvalue.get().isdigit():
                        value = int(scvalue.get())
                    else:
                        value = eval(screen.get())

                    scvalue.set(value)
                    screen.update()
                elif text == "C":
                    scvalue.set("")
                    screen.update()

                else:
                    scvalue.set(scvalue.get() + text)
                    screen.update()

            root = Tk()
            root.geometry("650x950")
            root.title("Calculator for PBL")
            scvalue = StringVar()
            scvalue.set("")
            screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
            screen.pack(fill=X, ipadx=8, pady=10, padx=10)

            f = Frame(root, bg="grey")
            b = Button(f, text="9", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="8", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="7", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)

            f.pack()
            f = Frame(root, bg="grey")
            b = Button(f, text="6", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="5", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="4", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)

            f.pack()

            f = Frame(root, bg="grey")
            b = Button(f, text="3", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="2", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="1", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)

            f.pack()
            f = Frame(root, bg="grey")
            b = Button(f, text="0", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="-", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="*", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)

            f.pack()
            f = Frame(root, bg="grey")
            b = Button(f, text="/", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="%", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="=", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)

            f.pack()
            f = Frame(root, bg="grey")
            b = Button(f, text="C", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text="+", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)
            b = Button(f, text=".", padx=28, pady=18, font="lucida 35 bold")
            b.pack(side=LEFT, padx=18, pady=5)
            b.bind("<Button-1>", click)

            f.pack()

            root.mainloop()

        elif 'mail' in query:                                     # mail sender 
            import smtplib
            import speech_recognition as sr
            import pyttsx3
            from email.message import EmailMessage

            listener = sr.Recognizer()
            engine = pyttsx3.init()

            def talk(text):
                engine.say(text)
                engine.runAndWait()

            def get_info():
                try:
                    with sr.Microphone() as source:
                        print('listening...')
                        voice = listener.listen(source)
                        info = listener.recognize_google(voice)
                        print(info)
                        return info.lower()
                except:
                    print("user not found....")
                    return "None"

            def send_email(receiver, subject, message):                   #define a fuction send_email
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                # Make sure to give app access in your Google account
                server.login('yudhishthirpbl@gmail.com', 'firstpandav')
                email = EmailMessage()
                email['From'] = 'yudhishthirpbl@gmail.com'
                email['To'] = receiver
                email['Subject'] = subject
                email.set_content(message)
                server.send_message(email)

            email_list = {                                                # data list 
                'yash': 'yashpkulkarni@gmail.com',
                'shridhar': 'diamond@bts.com',
                'prasad': 'prasadunecha16@gmail.com',
                'network': 'unechanetworking@gmail.com',
                'mohit': 'mohitkunecha@gmail.com',
                'balaji': 'balajivaste212@gmail.com',
                'pratham': 'prathu2mk@gmail.com'
            }

            def get_email_info():
                talk('To Whom you want to send email')
                name = get_info()
                
                if (name in email_list.keys()):       
                    receiver = email_list[name]
                    print(receiver)
                    talk('What is the subject of your email?')
                    subject = get_info()
                    talk('Tell me  text in your email')
                    message = get_info()
                    send_email(receiver, subject, message)
                    talk('Friend . Your email is sent')
                    talk('Do you want to send more email?')
                    send_more = get_info()
                    if 'yes' in send_more:
                        get_email_info()

                else:
                    print('user not found, do you want to send to another user')
                    talk('User not found, do you want to send to another user')
                    def yesno():
                        send_more = get_info()
                        if 'yes' in send_more:
                            get_email_info()
                        elif 'no' in send_more:
                            print('thank you friend call me up for any email related issue')
                            speak('thank you friend call me up for any email related issue')
                            pass
                        else:
                            print('say yes or no ')
                            talk('say yes or no ')
                            yesno()
                    yesno()


            get_email_info()

        elif 'spam' in query:                                     # all apps spam or messaging bot
            speak('spamming')
            import pyautogui
            import webbrowser as wb
            import time
            pyautogui.hotkey('win','3')
            time.sleep(30)
            for i in range(5):
                pyautogui.press("W")
                pyautogui.press("E")
                pyautogui.press("L")
                pyautogui.press("C")
                pyautogui.press("O")
                pyautogui.press("M")
                pyautogui.press("E")
                pyautogui.press(" ")
                pyautogui.press("T")
                pyautogui.press("O")
                pyautogui.press(" ")
                pyautogui.press("P")
                pyautogui.press("I")
                pyautogui.press("C")
                pyautogui.press("T")

                pyautogui.press("enter")

        elif 'location' in query:                                 # find location of any place
            # to find location of any place
            speak('can you tell the name of the place you are searching for ?')
            location = takeCommand('can you tell the name of the place you are searching for ?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of ' + location)
            speak('Here is the location of' + location)

        elif 'phone' in query:                                   # price tracker 
            speak('checking price')
            print('Checking....')
            import requests
            from bs4 import BeautifulSoup
            from email_alert import alert_system
            from threading import Timer

            URL = "https://www.amazon.in/OnePlus-Nord-Sierra-128GB-Storage/dp/B097RDVDL2/ref=lp_1389401031_1_4"

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip',
                'DNT': '1',  # Do Not Track Request Header
                'Connection': 'close'
            }

            set_price = 28000
            speak('ur Phone is ')

            def check_price():
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')

                title = soup.find(id='productTitle').get_text()
                product_title = str(title)
                product_title = product_title.strip()
                print(product_title)
                price = soup.find(id='priceblock_dealprice').get_text()
                # print(price)
                product_price = ''
                for letters in price:
                    if letters.isnumeric() or letters == '.':
                        product_price += letters
                print(float(product_price))
                if float(product_price) <= set_price:
                    alert_system(product_title, URL)
                    print(' Boss your products price has been droped ,Mail sent')
                    speak('Boss your products price has been droped, Mail send with link address of the product')
                    return
                else:
                    print('Mail not sent')
                    speak('Boss your products price is high. check again later')
                #Timer(60, check_price).start()

            check_price()
            
        elif 'cal' in query:                                      # opens microsoft inbuild calcuator
            import autoit
            import pyautogui

            pyautogui.hotkey('win', 'r')
            pyautogui.press('backspace')

            autoit.control_focus("Run", "Edit1")
            autoit.control_set_text("Run", "Edit1", "Calc")
            autoit.control_click("Run", "Button2")
        
        elif 'game' in query:
            import time
            import random

            # welcome script
            time.sleep(1.5)
            print('-----------------------------------Welcome to Tic-Tac-Toe-----------------------------------')
            speak('Welcome to Tic-Tac-Toe')
            time.sleep(0.5)
            print('This game is made by my friends\n')
            speak('This game is made by my friends')

            # variable's
            win = 0
            lose = 0
            X = 'X'
            O = 'O'


            # definitions
            def win_check():
                global r1, r2, r3, r4, r5, r6, r7, r8, r9
                global X_win, O_win, tie
                global u_name, u2_name
                global win
                if r1 == 'X' and r2 == 'X' and r3 == 'X':
                    X_win = True
                elif r4 == 'X' and r5 == 'X' and r6 == 'X':
                    X_win = True
                elif r7 == 'X' and r8 == 'X' and r9 == 'X':
                    X_win = True
                elif r1 == 'X' and r4 == 'X' and r7 == 'X':
                    X_win = True
                elif r2 == 'X' and r5 == 'X' and r8 == 'X':
                    X_win = True
                elif r3 == 'X' and r6 == 'X' and r9 == 'X':
                    X_win = True
                elif r1 == 'X' and r5 == 'X' and r9 == 'X':
                    X_win = True
                elif r3 == 'X' and r5 == 'X' and r7 == 'X':
                    X_win = True
                elif r1 == 'O' and r2 == 'O' and r3 == 'O':
                    O_win = True
                elif r4 == 'O' and r5 == 'O' and r6 == 'O':
                    O_win = True
                elif r7 == 'O' and r8 == 'O' and r9 == 'O':
                    O_win = True
                elif r1 == 'O' and r4 == 'O' and r7 == 'O':
                    O_win = True
                elif r2 == 'O' and r5 == 'O' and r8 == 'O':
                    O_win = True
                elif r3 == 'O' and r6 == 'O' and r9 == 'O':
                    O_win = True
                elif r1 == 'O' and r5 == 'O' and r9 == 'O':
                    O_win = True
                elif r3 == 'O' and r5 == 'O' and r7 == 'O':
                    O_win = True
                if O_win:
                    win = True
                    speak('Winner is')
                    return print('Winner is', u2_name.upper()), win
                if X_win:
                    win = True
                    speak('Winner is')
                    return print('Winner is', u_name.upper(), '\n--Game Ends--\n'), win
                if r1 != '-' and r2 != '-' and r3 != '-' and r4 != '-' and r5 != '-' and r6 != '-' and r7 != '-' and r8 != '-' and r9 != '-':
                    tie = True
                    speak('This game is a tie')
                    return print('This game is a tie'), tie


            def rule():
                print('It seems you have some Trouble while play game, no worry i will help you.')
                speak('It seems you have some Trouble while play game, no worry i will help you.')
                print('In Tic-Tac-Toe you have to make a straight line out of 3-O or 3-X')
                speak('In Tic-Tac-Toe you have to make a straight line out of 3-O or 3-X')
                print('For example:')
                speak('For example:')
                print(" X | O | X \n ---------- \n X | X | O \n ----------\n X | O | O \n")


            def check_game_o():
                global r1, r2, r3, r4, r5, r6, r7, r8, r9, command_2
                retry_check = False
                if command_2 == 1 and r1 == '-':
                    r1 = O
                elif command_2 == 2 and r2 == '-':
                    r2 = O
                elif command_2 == 3 and r3 == '-':
                    r3 = O
                elif command_2 == 4 and r4 == '-':
                    r4 = O
                elif command_2 == 5 and r5 == '-':
                    r5 = O
                elif command_2 == 6 and r6 == '-':
                    r6 = O
                elif command_2 == 7 and r7 == '-':
                    r7 = O
                elif command_2 == 8 and r8 == '-':
                    r8 = O
                elif command_2 == 9 and r9 == '-':
                    r9 = O
                elif command_2 == 1 and r1 != '-' or command_2 == 2 and r2 != '-' or command_2 == 3 and r3 != '-' or command_2 == 4 and r4 != '-' or command_2 == 5 and r5 != '-' or command_2 == 6 and r6 != '-' or command_2 == 8 and r8 != '-' or command_2 == 7 and r7 != '-' or command_2 == 9 and r9 != '-':   
                    while not retry_check:
                        command_2 = int(input("Don't be Over smart! Try a place which is available as you can not over write a "
                                            "place: "))          
                        check_game_o()
                        retry_check = True
                elif command_2 > 9:
                    retry_check = False
                    while not retry_check:
                        command_2 = int(input("Please select a number between 1-9 ONLY: "))
                        check_game_o()
                        retry_check = True

                return r1, r2, r3, r4, r5, r6, r7, r8, r9


            def check_game_x():
                global r1, r2, r3, r4, r5, r6, r7, r8, r9, command
                retry_check = False
                if command == 1 and r1 == '-':
                    r1 = X
                elif command == 2 and r2 == '-':
                    r2 = X
                elif command == 3 and r3 == '-':
                    r3 = X
                elif command == 4 and r4 == '-':
                    r4 = X
                elif command == 5 and r5 == '-':
                    r5 = X
                elif command == 6 and r6 == '-':
                    r6 = X
                elif command == 7 and r7 == '-':
                    r7 = X
                elif command == 8 and r8 == '-':
                    r8 = X
                elif command == 9 and r9 == '-':
                    r9 = X
                elif command == 1 and r1 != '-' or command == 2 and r2 != '-' or command == 3 and r3 != '-' or command == 4 and r4 != '-' or command == 5 and r5 != '-' or command == 6 and r6 != '-' or command == 8 and r8 != '-' or command == 7 and r7 != '-' or command == 9 and r9 != '-':
                    while not retry_check:
                        command = int(input("Don't be Over smart! Try a place which is available as you can not over write a "
                                            "place: "))
                        check_game_x()
                        retry_check = True
                elif command > 9:
                    retry_check = False
                    while not retry_check:
                        command = int(input("Please select a number between 1-9 ONLY: "))
                        check_game_x()
                        retry_check = True
                return r1, r2, r3, r4, r5, r6, r7, r8, r9


            def computer_turn():
                global r1, r2, r3, r4, r5, r6, r7, r8, r9, command_2
                global comp_turn
                comp_turn = False
                while not comp_turn:
                    command_2 = random.randrange(1, 10)
                    if command_2 == 1 and r1 == '-':
                        r1 = O
                        comp_turn = True
                    elif command_2 == 2 and r2 == '-':
                        r2 = O
                        comp_turn = True
                    elif command_2 == 3 and r3 == '-':
                        r3 = O
                        comp_turn = True
                    elif command_2 == 4 and r4 == '-':
                        r4 = O
                        comp_turn = True
                    elif command_2 == 5 and r5 == '-':
                        r5 = O
                        comp_turn = True
                    elif command_2 == 6 and r6 == '-':
                        r6 = O
                        comp_turn = True
                    elif command_2 == 7 and r7 == '-':
                        r7 = O
                        comp_turn = True
                    elif command_2 == 8 and r8 == '-':
                        r8 = O
                        comp_turn = True
                    elif command_2 == 9 and r9 == '-':
                        r9 = O
                        comp_turn = True
                return r1, r2, r3, r4, r5, r6, r7, r8, r9, print('I choose', command_2)


            def write_log():
                global u_name, u2_name, X_win, O_win
                global r1, r2, r3, r4, r5, r6, r7, r8, r9
                log = open('log.txt', 'a')
                log.seek(0)
                if X_win:
                    vb = u_name
                elif O_win:
                    vb = u2_name
                else:
                    vb = 'Tie'
                log.write('\n {} vs {} | {}'.format(u_name, u2_name, vb).upper())
                log.seek(0)
                log.write("\n\n {} | {} | {} \n ---------- \n {} | {} | {} \n ----------\n {} | {} | {}\n\n\n".format(r1, r2, r3, r4, r5, r6, r7, r8, r9))


            def read_log():
                log = open('log.txt', 'r')
                log.seek(0)
                print('\n\n')
                print(log.read(),'\n\n')


            rule()
            time.sleep(0.5)
            print('Type * -h or help * to see how to play this Game...')
            time.sleep(0.5)
            while True:
                r1 = '-'
                r2 = '-'
                r3 = '-'
                r4 = '-'
                r5 = '-'
                r6 = '-'
                r7 = '-'
                r8 = '-'
                r9 = '-'
                u_name = 'Player 1'
                u2_name = 'Player 2'
                X_win = False
                O_win = False
                comp_turn = False
                win = False
                tie = False

                input_1 = takeCommand()
                if input_1 == '-h' or input_1 == 'help' or input_1 == 'options':
                    print('Welcome to Help box:)')
                    speak('Welcome to Help box')
                    print('Here are all options and everything you can do with this Game.\n')
                    speak('Here are all options and everything you can do with this Game')
                    print('-----------------------------------------------------------------------')
                    print('| Options                 | Use                                       |')
                    print('-----------------------------------------------------------------------')
                    print('| -h or help              | To see all available options for the game.|')
                    print('''| About                   | To see information about the developer of |
            |                         | this Game                                 |''')
                    print('| Start game or New game  | To start a new game.                      |')
                    print('| Log/stats/db_load       | To see previous stats of the game.                |')
                    print('| Rule                    | To Know rules of the game.                |')
                    print('| Exit or Quit            | To Quit/Exit the game.                    |')
                    print('-----------------------------------------------------------------------\n')
                elif input_1 == 'log' or input_1 == 'logs' or input_1 == 'db_load' or input_1 == 'stats':
                    print('reading database...')
                    speak('reading database...')
                    time.sleep(2)
                    read_log()
                elif input_1 == 'about':
                    print('Hello,')
                    speak('Hello,')
                    print('      My self Tic-tac-toe and I was created by Yudhishthir.')
                    speak('My self Tic-tac-toe and I was created by Yudhisthir.')
                    print('E-mail: yudhishthirpbl@gmail.com')
                elif input_1 == 'exit' or input_1 == 'quit' or input_1 == 'clear' :
                    #exit()
                    break
                    
                elif input_1 == 'start game' or input_1 == 'new game' or input_1 == 'game play' or input_1 == 'game start':
                    duo_ai = input('Would you link to play with your friend or bot(f/b): ')
                    if duo_ai == 'friend' or duo_ai == 'f' or duo_ai == 'my friend' or duo_ai == 'duo' or duo_ai == 'human':
                        game_on = True
                        print('Hello, I am Yudhishthir and i am your umpire today.')
                        u_name = input('What should i call you player 1(X)? ')
                        u2_name = input('What should i call you player 2(O)? ')
                        print("let's see who wins today.")
                        speak("let's see who wins today.")
                        print("let's start with the game now", u_name.upper(), 'vs', u2_name.upper(), '\n\n')
                        speak("let's start with the game now")
                        print("Type 'Rule' to see Rules.")
                        print(' ', 1, '|', 2, '|', 3, '\n ---------- \n', '', 4, '|', 5, '|', 6, '\n ----------\n', '', 7,
                            '|', 8, '|', 9, '\n')
                        while game_on:
                            command = int(input('>> Please enter the position you want to place the X to(1-9 only): '))
                            check_game_x()
                            print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',
                                r7, '|', r8, '|', r9, '\n')

                            win_check()
                            if win or tie:
                                write_log()
                                break

                            command_2 = int(input('>> Please enter the position you want to place the O to(1-9 only): '))
                            check_game_o()
                            print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',
                                r7, '|', r8, '|', r9, '\n')

                            win_check()
                            if win or tie:
                                write_log()
                                break

                    elif duo_ai == 'computer' or duo_ai == 'bot' or duo_ai == 'ai' or duo_ai == 'single' or duo_ai == 'b':
                        print('Hello, I am Yudhishthir and i am your opponent today.')
                        speak('what should i call you? ')
                        u_name = input('What should i call you? ')
                        print("let's see if you can beat me.")
                        speak("let's see if you can beat me.")
                        u2_name = 'bot'
                        print("let's start with the game now", u_name.upper(), '\n\n')
                        print("Type 'Rule' to see Rules.")
                        print(' ', 1, '|', 2, '|', 3, '\n ---------- \n', '', 4, '|', 5, '|', 6, '\n ----------\n', '', 7,
                            '|', 8, '|', 9, '\n')
                        game_on = True
                        while game_on:
                            command = int(input('>> Please enter the position you want to place the X to(1-9 only): '))
                            check_game_x()
                            print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',
                                r7, '|', r8, '|', r9, '\n')

                            win_check()
                            if win or tie:
                                write_log()
                                break

                            print("It's my turn now")
                            speak("It's my turn now")
                            computer_turn()

                            print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',
                                r7, '|', r8, '|', r9, '\n')
                            win_check()
                            if win or tie:
                                write_log()
                                break

                elif input_1 == 'rule' or input_1 == 'rules':
                    rule()
                else:
                    print("It's seems some error occurred, please check your spellings.")
                    speak("It's seems some error occurred, please check your spellings.")
     
        elif 'rock' in query:                                     # rock paper scissor game through voice commands
            from games import rps
            speak('Friend lets play a game   lets play rock paper scissor')
            print('playing game')
            rps()
               
        elif 'weather' in query:                                  # wheather focast of any city of any country
            import requests
            from pprint import pprint
            def weather_data(query):
                res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
                return res.json();
            def print_weather(result,city):
                print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
                speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
                print("Wind speed: {} m/s".format(result['wind']['speed']))
                speak("Wind speed: {} meter per second".format(result['wind']['speed']))
                print("Description: {}".format(result['weather'][0]['description']))
                speak("Description: {}".format(result['weather'][0]['description']))
                print("Weather: {}".format(result['weather'][0]['main']))
                speak("Weather: {}".format(result['weather'][0]['main']))
            def main():
                speak('enter the city name')
                city=input('Enter the city:')
                print()

                try:
                    query='q='+city;
                    w_data=weather_data(query);
                    print_weather(w_data, city)
                    print()
                except:
                    print('City name not found...')
            if __name__=='__main__':
                main()

        elif 'security' in query:
            from camera import security
            speak('opening surveillance system and keeping an eye')
            print('opening surveillance system and keeping an eye')
            security()
            
            
                                      
        elif 'bye' in query:                                      # exit message
            speak('thank you Friend')
            exit()
