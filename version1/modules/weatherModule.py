import threading
import time
import sched
import datetime
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel
from kivy.graphics import *
from settingsReader import readSecretAttribute
import sqlite3
import requests

class openWeatherApi:
    def __init__(self,apikey):
        self.apikey = apikey

    def getDailyWeather(self):
        pass

    def getWeeklyWeather(self):
        pass 

#Updates the button and is executed from a thread
class weatherThread:
    def __init__(self, button):
        print("Updated Button")
        self.button = button
       
    
    def update(self):
        pass
        
    def run(self):
        while 1:
            threading.Timer(30,self.run)
            self.update()
            time.sleep(30)

#This controls the default screen that is generated when the button is pressed
class weatherScreen(Screen):

    def __init__(self,sm,**kwargs):
        super(weatherScreen, self).__init__(**kwargs)
        self.sm = sm
        layout = BoxLayout()
        self.add_widget(layout)
        
        
        backButton = Button(text='Back', font_size=20)
        backButton.bind(on_press = self.callback)
        layout.add_widget(backButton)

    def callback(self,x):
        self.sm.current = "menu"


if __name__ == "__main__":
    t = weatherThread("test")
    threading.Thread(target=t.run).start()
