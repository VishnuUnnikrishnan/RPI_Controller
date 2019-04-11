import threading
import time
import sched
import datetime
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


#Updates the button and is executed from a thread
class clockThread:
    def __init__(self, button):
        self.button = button   
    
    def update(self):
        x = datetime.datetime.now()
        self.button.text = x.strftime("%A %d %B\n%H:%M")
        print(x.strftime("%A %d %B\n%H:%M"))
    
        
    def run(self):
        while 1:
            threading.Timer(30,self.run)
            self.update()
            time.sleep(30)

#This controls the default screen that is generated when the button is pressed
class clockScreen(Screen):

    def __init__(self,sm,**kwargs):
        super(clockScreen, self).__init__(**kwargs)
        self.sm = sm
        layout = GridLayout(rows=1)
        self.add_widget(layout)
        backButton = Button(text='Back', font_size=20)
        backButton.bind(on_press = self.callback)
        layout.add_widget(backButton)

    def callback(self,x):
        self.sm.current = "menu"


if __name__ == "__main__":
    t = clockThread("test")
    threading.Thread(target=t.run).start()
