from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window
from settingsReader import readAttribute
from modules.clockModule import clockThread

import threading

__moduleSettings__ = {}

def getData():
    global __moduleSettings__
    __moduleSettings__ = readAttribute("main_settings")
    return

getData()

# Declare both screens
class MenuScreen(Screen):
    def __init__(self,**kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        global __moduleSettings__
        rows = int(__moduleSettings__["row"])
        cols = int(__moduleSettings__["col"])
        
        layout = GridLayout(rows=rows, cols=cols)
        self.add_widget(layout)
        for i in range(0,rows*cols):
            button = Button(text='Button '+str(i), font_size=20)
            self.connectModule(button,i)
            layout.add_widget(button)

    def connectModule(self, button, id):
        if id == 0:
            t = clockThread(button)
            threading.Thread(target=t.clock).start()
        


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

class rpiDisplay(App):

    def build(self):
        return sm

if __name__ == '__main__':
    #Window.fullscreen = 'auto'
    rpiDisplay().run()