import speech_recognition as sr
import os
import sys
import re
import webbrowser
import subprocess
import Therabot

def sofiaResponse(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


def myCommand():
    "listens for commands"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command


def assistant(command):
    "if statements for executing commands"
    #shutdown
    if('shutdown') in command:
            sofiaResponse('Bye bye Sir. Have a nice day')
            sys.exit()

    #open website

    elif('open') in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain
                webbrowser.open(url)
                sofiaResponse('The website you have requested has been opened for you Sir.')

    elif('launch therapy session' or 'i want to go in for therapy') in command:
        return Therabot.Therabot()

    elif 'help me' in command:
        sofiaResponse("""
        You can use these commands and I'll help you out:
        1. Open : Opens the Website in default browser.
        2. Open xyz.com : replace xyz with any website name
        3. Launch Therapy Session : Executes the Module for Therapy, content will be asked in order.
        """)

    #launch any application
    elif('launch') in command:
        reg_ex = re.search('launch (.*)', command)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname+".exe"
            subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
    sofiaResponse('I have launched the desired application')




def main():
    sofiaResponse('Hi, I am Therabot''s personal Voice Assistant, '
                  'Please give a command or say "help me" and I will tell you what all I can do for you.')
    #loop to continue executing multiple commands
    while True:
        assistant(myCommand())



if __name__ == '__main__':
    main()
