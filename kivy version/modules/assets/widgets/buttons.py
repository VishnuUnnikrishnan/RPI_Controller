"""
This is a text Button, that contains a text element that can
be updated by the caller
"""

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import *

class textButton(Widget):
    #Create Button on initialisation
    def __init__(self, **kw):
        super(textButton, self).__init__(**kw)
        topLayout=BoxLayout(orientation = "vertical")
        self.add_widget(topLayout)
        topLayout.add_widget(Label(text='Hello world', font_size='20sp'))
        topLayout.add_widget(Label(text='Hello world', font_size='20sp'))
        topLayout.add_widget(Label(text='Hello world', font_size='20sp'))

        self.pos_hint = {"top":"1"}