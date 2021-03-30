from os import environ
from hashlib import sha384
from time import time
from pynput.keyboard import Key, Listener
from string import ascii_letters
from threading import Thread
from sys import exit
from win10toast import ToastNotifier
from playsound import playsound
from subprocess import call

class tools(object):

    def __init__(self, TimeBounes):
        self.time = (time() + TimeBounes)
        self.password = environ.get('ideal')
        self.password_match = ''

    def TimeProcess(self, source):
        source.start()
        while(self.time > time()):
            if self.password == sha384(self.password_match.encode()).hexdigest():
                return True
        if self.password ==  sha384(self.password_match.encode()).hexdigest():
            return True
        else:
            return False
    def press(self, key):
        key = str(key)
        if key == "Key.tab":
            self.password_match = ''
            toaster.show_toast("Windows 10", "clean Keyboard!", threaded=True, icon_path=None, duration=3)
        else:   
            self.password_match += key[1:-1]

toaster = ToastNotifier()
use  = tools(20)
with Listener(on_press=use.press) as keyboard:
    SOURCE = Thread(target=keyboard.join)
    if use.TimeProcess(SOURCE) == True:
        toaster.show_toast("Windows 10", "successfully You Have Access !", threaded=True, icon_path=None, duration=5)
        playsound('https://audio-previews.elements.envatousercontent.com/files/116837282/preview.mp3')
    else:
        call('shutdown /f /s /t 10')
        toaster.show_toast("Windows 10", "Worng You Need left my pc !", threaded=True, icon_path=None, duration=5)
        playsound('https://audio-previews.elements.envatousercontent.com/files/270924693/preview.mp3')
