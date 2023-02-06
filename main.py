#HACKATHON PROJECT CONDUCTED BY HEADOUT

import playsound
from playsound import playsound
import pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from gtts import gTTS
import os
import AppOpener
import tkinter
import cv2
def lizzie():
    query = ''
    print('\n')
    print(
        "                                                                        STARTING YOUR PROJECT.........                                            ")
    print('\n')

    def response():

        k = wikipedia.summary(query, sentences=2)
        print(k)
        engine = pyttsx3.init()
        engine.say(k)

        engine.runAndWait()

    k = 'hey user....................i m listening to you.........................lets have a  conversation........................'
    engine = pyttsx3.init()
    engine.say(k)
    engine.runAndWait()

    while True:

        print("listening.....!!")
        r = sr.Recognizer()
        m=''
        i=0
        while i<100:
            from playsound import playsound
            playsound()
            print("listening.....!!")

            try:
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    audio2 = r.listen(source2)
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()

                    print("Bhai tuune " + MyText, "bola kya?")
                    query = MyText
                    try:
                        from googlesearch import search
                    except ImportError:
                        print("working on your command!!")

                    if 'who is' in query:
                        query = query.replace('who is', "")
                        print(query)
                        response()
                    elif 'how are you' in query:
                        k = 'working at my best...............what about you '
                        print(k)
                        engine = pyttsx3.init()
                        engine.say(k)
                        engine.runAndWait()

                    elif 'feeling sad' in query:
                        k = 'life is just a game.......................just smile............because yours is the reason for mine'
                        print("")
                        engine = pyttsx3.init()
                        engine.say(k)
                        engine.runAndWait()
                    elif 'tell me' in query:
                        query = query.replace('tell me', "")
                        response()
                    elif 'hey' in query:
                        k = 'hello user............nice to meet you'
                        print(k)
                        engine = pyttsx3.init()
                        engine.say(k)
                        engine.runAndWait()
                    elif 'feeling sad' in query:
                        k = 'life is just a game.......................just smile............because yours is the reason for mine'
                        print(k)
                        engine = pyttsx3.init()
                        engine.say(k)
                        engine.runAndWait()
                    elif 'hii' in query:
                        k = 'hello user............nice to meet you'
                        print(k)
                        engine = pyttsx3.init()
                        engine.say(k)
                        engine.runAndWait()
                    elif 'hello' in query:
                        k = 'hello user............nice to meet you'
                        print(k)
                        engine = pyttsx3.init()
                        engine.say(k)
                        engine.runAndWait()
                    elif 'tell me about' in query:
                        query = query.replace('tell me about', "")
                        response()
                    elif 'search' in query:
                        query = query.replace('search', '')
                        response()
                    elif 'play a song' in query:
                        print("playing some random song from famous searches....!!")
                        query = query.replace('play a song', 'close eyes')
                        pywhatkit.playonyt(query)
                    elif 'play' in query:
                        query = query.replace('play', '')
                        pywhatkit.playonyt(query)

                    elif 'love you' in query:
                        k = 'lets first spend some time together'
                        print(k)
                        engine = pyttsx3.init()
                        engine.say(k)
                        engine.runAndWait()
                    elif 'fuck you' in query:
                        k = 'lets give it a chance'
                        print(k)
                        engine = pyttsx3.init()
                        engine.say(k)
                        engine.runAndWait()
                    elif 'open' in query:
                        query = query.replace('open', '')
                        from AppOpener import run

                        run(query)
                    elif 'run' in query:
                        query = query.replace('run', '')
                        from AppOpener import run

                        run(query)
                    elif 'send a mail' in query:


                        class MyWindow:
                            def __init__(self, win):
                                self.lbl1 = Label(win, text='RECIEVERS ADDRESS: ')
                                self.lbl2 = Label(win, text='MESSAGE: ')
                                self.lbl3 = Label(win, text='CONCLUSION: ')
                                self.t1 = Entry(bd=3)
                                self.t2 = Entry()
                                self.t3 = Entry()
                                self.btn1 = Button(win, text='SEND A MAIL')
                                self.lbl1.place(x=100, y=50)
                                self.t1.place(x=200, y=50)
                                self.lbl2.place(x=100, y=100)
                                self.t2.place(x=200, y=100)
                                self.b1 = Button(win, text='SEND A MAIL', command=self.add)
                                self.b1.place(x=100, y=150)

                                self.lbl3.place(x=100, y=200)
                                self.t3.place(x=200, y=200)

                            def add(self):
                                self.t3.delete(0, 'end')
                                address = (self.t1.get())
                                message = (self.t2.get())
                                import smtplib

                                send = "yadavashutoshup12@gmail.com"
                                rec = address
                                pas = "vkiw jxcn xrpt fpde"
                                message = message
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(send, pas)
                                server.sendmail(send, rec, message)
                                result = "mail send successfully"
                                self.t3.insert(END, str(result))

                        window = Tk()
                        mywin = MyWindow(window)
                        window.title('Hello Python')
                        window.geometry("400x300+10+10")
                        window.mainloop()
                    elif 'set reminder at' in query:
                        query = query.replace('set reminder at','')
                        if 'pm' in query:
                            import datetime
                            from playsound import playsound
                            Hour = int(input())
                            Min = int(input())
                            ty = input("pm/am")

                            if ty == "pm":
                                alarmHour += 12

                            while True:
                                if Hour == datetime.datetime.now().hour and Min == datetime.datetime.now().minute:
                                    print("Playing alarm... ")
                                    playsound("C:\CODE KRLO\pythonProject2\cone.mp3")
                                    break


                    elif 'set alarm at' in query:
                        query = query.replace('set alarm at','')
                        if 'pm' in query:
                            import datetime
                            from playsound import playsound
                            Hour = int(input())
                            Min = int(input())
                            ty = 'pm'


                            alarmHour += 12

                            while True:
                                if Hour == datetime.datetime.now().hour and Min == datetime.datetime.now().minute:
                                    print("Playing alarm... ")
                                    playsound("C:\CODE KRLO\pythonProject2\cone.mp3")
                                    break
                        elif 'am' in query:
                            query = query.replace('set alarm at', '')
                            import datetime
                            from playsound import playsound
                            Hour = int(input())
                            Min = int(input())
                            ty = 'am'


                            alarmHour += 12

                            while True:
                                if Hour == datetime.datetime.now().hour and Min == datetime.datetime.now().minute:
                                    print("Playing alarm... ")
                                    playsound("C:\CODE KRLO\pythonProject2\cone.mp3")
                                    break


                    else:
                        response()


            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                m = 'there some network issue.............................................please try again'
                print(m)
                engine = pyttsx3.init()
                engine.say(m)

                engine.runAndWait()
            if 'there some network issue.............................................please try again' in m:
                i=i+1




while True:

    import cv2

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("VERIFICATION")


    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.setWindowProperty("VERIFICATION", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

    import face_recognition

    known_image = face_recognition.load_image_file("opencv_frame_0.png")
    unknown_image1 = face_recognition.load_image_file("C:\lace detection\l2\cest.jpeg")
    unknown_image2 = face_recognition.load_image_file("C:\lace detection\l3\ik.jpeg")
    unknown_image3 = face_recognition.load_image_file("C:\lace detection\l4\cest3.jpeg")
    unknown_image4 = face_recognition.load_image_file("C:\lace detection\l5\cest4.jpeg")

    encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image1)[0]

    results = face_recognition.compare_faces([encoding], unknown_encoding)
    # print(results)
    if results == [True]:
        print("user found : arjun")
        lizzie()

    elif results == [False]:
        encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image2)[0]

        results = face_recognition.compare_faces([encoding], unknown_encoding)
        if results == [True]:
            print("user found : arnik")
            lizzie()

        elif results == [False]:
            encoding = face_recognition.face_encodings(known_image)[0]
            unknown_encoding = face_recognition.face_encodings(unknown_image3)[0]
            if results == [True]:
                print("user found : Ritee")
                lizzie()
            elif results == [False]:
                encoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_image4)[0]
                if results == [True]:
                    print("user found : shivani")
                    lizzie()

                else:
                    k = 'unauthorized user.........................access denied............................try again'
                    print(k)

                    engine = pyttsx3.init()
                    engine.say(k)
                    engine.runAndWait()
                    print(k)
