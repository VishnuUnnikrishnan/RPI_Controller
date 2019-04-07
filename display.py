from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window
from settingsReader import readAttribute
from functools import partial
import imp
import logging
import threading

__moduleSettings__ = {}
# Create the screen manager
sm = ScreenManager()

def getData():
    global __moduleSettings__
    __moduleSettings__ = readAttribute("main_settings")
    return

getData()

# Declare initial screens
class MenuScreen(Screen):
    def __init__(self,**kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        global __moduleSettings__
        rows = int(__moduleSettings__["row"])
        cols = int(__moduleSettings__["col"])
        
        layout = GridLayout(rows=rows, cols=cols)
        self.add_widget(layout)
        for i in range(0,rows*cols):
            #set default button fields here, can be updated by user
            button = Button(text='Button '+str(i), font_size=20, halign="center")
            self.connectModule(button,i)
            layout.add_widget(button)

    def connectModule(self, button, id):
        global __moduleSettings__
        try:
            #Load Module
            moduleName = __moduleSettings__["module_"+str(id)]
            newModule = readAttribute("modules."+ moduleName)
            module = imp.load_source(moduleName,"modules/"+moduleName+".py")
            #Load class to be run
            executeClass = getattr(module, newModule["class"])
            
            #Load Display for button click
            displayClass = getattr(module, newModule["screen"])
            sm.add_widget(displayClass(sm=sm, name = newModule["screen"]))

            #Pass change screen from menu button to the context that was selected.
            button.bind(on_press =partial(self.changeScreen, newModule["screen"]))
            
            #Run Module Code
            t = executeClass(button)
            threading.Thread(target=t.run).start()

        except:
            print("Error: No module_"+str(id)+" found")
        
    def changeScreen(self, x, id):
        print(type(x))
        sm.current = x

sm.add_widget(MenuScreen(name="menu"))
#sm.current = "menu"

class rpiDisplay(App):

    def build(self):
        return sm

if __name__ == '__main__':
    #Window.fullscreen = 'auto'
    rpiDisplay().run()