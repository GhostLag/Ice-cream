import numpy as np
import pandas as pd

import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.textinput import TextInput

# Edit backgroundRGBA values to change the RGBA values for the background
backgroundRGBA = np.array([129, 57, 58, 255], dtype = float)
backgroundColour = np.divide(backgroundRGBA, 255)
Window.clearcolor = (list(backgroundColour))

kv = '''
<ColoredLabel>:
    background_color:
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
'''

Builder.load_string(kv)

class ColoredLabel(Label):
    background_color = ListProperty((0, 0, 0, 1))


class MainInterface(BoxLayout, Screen):

  def importInterface(self, event):
    self.parent.current = 'importInterface' 

  def calculateBatchesInterface(self, event):
    self.parent.current = 'calculateBatchesInterface'

  def __init__(self, **kwargs):
    super().__init__(**kwargs)

    title = ColoredLabel(text = f"[color=debf76]Ice Cream Calculator[/color]",
            background_color = (140/255, 78/255, 79/255, 1),
            font_size = '40dp',
            markup = True,
            pos_hint = {'center_x': .5},
            size_hint = (.7, .4))

    btn1 = Button(text = "[color=ddb975]Import Data[/color]",
            background_color = (140/255, 78/255, 79/255, .5),
            font_size = '30dp',
            markup = True,
            pos_hint = {'center_x': .5},
            size_hint = (.55, .2))
    btn2 = Button(text = "[color=ddb975]Calculate Ice Cream Batches[/color]",
            background_color = (140/255, 78/255, 79/255, .5),
            font_size = '30dp',
            markup = True,
            pos_hint = {'center_x': .5},
            size_hint = (.55, .2))

    btn1.bind(on_press = self.importInterface)
    btn2.bind(on_press = self.calculateBatchesInterface)

    self.spacing = '30dp'
    self.orientation = "vertical"

    self.add_widget(title)
    self.add_widget(btn1)
    self.add_widget(btn2)

class ImportInterface(BoxLayout, Screen):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)

    l1 = Label(text = "test")
    self.add_widget(l1)

class CalculateBatchesInterface(BoxLayout, Screen):
    pass

class IceCreamApp(App):

  def build(self):
    '''
    foo = np.array([1, 3, 4, 2, 4])
    foo1 = np.multiply(foo, 2)
    return Label(text = f"[color=debf76]{foo} * 2\n{str(foo1)}[/color]", font_size = '25sp', markup = True)
    '''

    screenManager = ScreenManager(transition = SlideTransition())
    screenManager.add_widget(MainInterface(name = "mainInterface"))
    screenManager.add_widget(ImportInterface(name = "importInterface"))
    screenManager.add_widget(CalculateBatchesInterface(name = "calculateBatchesInterface"))

    return screenManager

IceCreamApp().run()
