from main import model, stream
import speech_recognition as sr   # voice recognition library
import random                     # to choose random words from list
import pyttsx3                    # offline Text to Speech
import datetime                   # to get date and time
import webbrowser                 # to open and perform web tasks
import serial                     # for serial communication
try:
    import pywhatkit              # for more web automation
except:
    pass

# Declare robot name (Wake-Up word)
robot_name = __file__.split('\\')[-1][:-3]
print(robot_name)

# random words list
hi_words = ['hi', 'hello', 'yo baby', 'salam']
bye_words = ['bye', 'tata', 'hasta la vista']
r_u_there = ['are you there', 'you there']

# initilize things
engine = pyttsx3.init()                    # init text to speech engine
voices = engine.getProperty('voices')      # check for voices
engine.setProperty('voice', voices[1].id)  # female voice
listener = sr.Recognizer()                 # initialize speech recognition API

# connect with NiNi motor driver board over serial communication
try:
    port = serial.Serial("COM15", 9600)
    print("Phycial body, connected.")
except:
    port = open('nul', 'wb')
    print("Unable to connect to my physical body")


def listen():
        """ listen to what user says"""
        try:
                with sr.Microphone() as source:                         # get input from mic
                        print("Talk>>")
                        voice = listener.listen(source)                     # listen from microphone
                        command = listener.recognize_google(voice).lower()  # use google API
                        # all words lowercase- so that we can process easily
                        #command = command.lower()         
                        print(command)

                        # look for wake up word in the beginning
                        if (command.split(' ')[0] == robot_name):
                                # if wake up word found....
                                print("[wake-up word found]")
                                process(command)                 # call process funtion to take action
        except BaseException as e:
                print("\n" + repr(e).split("(")[0] + (":" if str(e) else ""), e)

def process(words):
        """ process what user says and take actions """
        print(words) # check if it received any command

        # break words in
        word_list = words.split(' ')[1:]   # split by space and ignore the wake-up word

        if (len(word_list)==0):
                if (words.split(' ')[0] == robot_name):
                    talk("How Can I help you?")
                    #.write(b'l')
                    return

        if word_list[0] == 'play':
                """if command for playing things, play from youtube"""
                talk("Okay boss, playing")
                extension = ' '.join(word_list[1:])                    # search without the command word
                port.write(b'u')
                pywhatkit.playonyt(extension)   
                port.write(b'l')          
                return

        elif word_list[0] == 'search':
                """if command for google search"""
                port.write(b'u')
                talk("Okay boss, searching")
                port.write(b'l')
                extension = ' '.join(word_list[1:])
                pywhatkit.search(extension)
                return

        if (word_list[0] == 'get') and (word_list[1] == 'info'):
                """if command for getting info"""
                port.write(b'u')
                talk("Okay, I am right on it")
                port.write(b'u')
                extension = ' '.join(word_list[2:])                    # search without the command words
                inf = pywhatkit.info(extension)
                talk(inf)                                              # read from result             
                return

        elif word_list[0] == 'open':
                """if command for opening URLs"""
                port.write(b'l')
                talk("Opening, sir")
                url = f"http://{''.join(word_list[1:])}"   # make the URL
                webbrowser.open(url)
                return

        elif word_list[0] == 'uppercut':
                port.write(b'U')
                return

        elif word_list[0] == 'smash':
                port.write(b's')
                return

        elif word_list[0] == 'punch':
                port.write(b'p')
                return

    # now check for matches
        for word in word_list:
                if word in hi_words:
                        """ if user says hi/hello greet him/her accordingly"""
                        port.write(b'h')               # send command to wave hand
                        talk(random.choice(hi_words))
                        return

                elif word in bye_words:
                        """ if user says bye etc"""
                        talk(random.choice(bye_words))
                        return

        try:
            response = stream(input=' '.join(word_list), model=model)
            for res in response:
                talk(res)
        except BaseException as e:
            talk(repr(e).split("(")[0])
            if str(e):
                talk(str(e))


def talk(sentence):
        """ talk / respond to the user """
        engine.say(sentence)
        engine.runAndWait()

# run the app
while True:
    listen()  # runs listen one time
