from buttons import textButton
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

sm = ScreenManager()

class MenuScreen(Screen):
    def __init__(self,**kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = GridLayout(rows=1, cols=1)
        self.add_widget(layout)
        layout.add_widget(textButton())

sm.add_widget(MenuScreen(name="menu"))
sm.current = "menu"

class Test(App):

    def build(self):
        return sm

if __name__ == '__main__':
    #Window.fullscreen = 'auto'
    Test().run()