import speech_recognition as sr                                 # Use for speech recongnization
import pyttsx3                                                  # Use for text to speech conversion
import datetime                                                 # Use for date & time
import pywhatkit                                                # Use for search on internet
import wikipedia                                                # Use for search on wikipedia
import pyjokes                                                  # Use for getting jokes from internet
import math


# Create listener variable for listening your voice
listener = sr.Recognizer()

alexa = pyttsx3.init()                                          # Initializing python text to speech
voices = alexa.getProperty('voices')                            # Calling python all voice propertied
alexa.setProperty('voice', voices[1].id)                        # Set female voice

# Define a function for text
def talk(text):
    alexa.say(text)                                             # Set a welcome tone
    alexa.runAndWait()

# Define a function for taking command
def take_command():
    try:
        with sr.Microphone() as source:                         # Connect microphone for listening your voice
            print('listening...') 
            voice = listener.listen(source)                     # Read your voice
            command = listener.recognize_google(voice)          # Convert your voice into text
            command = command.lower()                           # Convert your voice into lower case
            if 'alexa' in command:
                command = command.replace('alexa','')           # Remove alexa name 
    except:
        pass                                                    # If error occured pass the command
    return command

# Define a function for run a command
def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')     # from datetime library know time with str format
        print('Current time is '+time)
        talk('Current time is '+time)

    elif 'play' in command:
        song = command.replace('play', '')
        print('playing' + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)                                # pywhatkit search it on youtube

    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)                   # Give the details from wikipedia within one sentence
        print(info)
        talk(info)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())                                # Tell a joke from pyjokes

    elif 'i love you' in command:
        talk('I love you too vaiya')
        print('I love you too vaiya')

    elif 'whatsapp message' in command:
        talk("Sending your massege")
        pywhatkit.sendwhatmsg_instantly("+8801609291385", "Hello from Alexa")   


    elif 'math' in command:
        print("Value of pi:",math.pi)
        print("Value of sin(45):",math.sin(45))
        print("Value of cos(45):" ,math.cos(45))

    else:
        talk("Sorry I can't understand your command. But I can search it for you on google.")
        pywhatkit.search(command)                               # Search on google



run_alexa()