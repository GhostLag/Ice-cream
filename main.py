import numpy as np
import pandas as pd

import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

# Edit backgroundRGBA values to change the RGBA values for the background
backgroundRGBA = np.array([129, 57, 58, 255], dtype = float)
backgroundColour = np.divide(backgroundRGBA, 255)
Window.clearcolor = (list(backgroundColour))

class IceCreamApp(App):

  def build(self):
    foo = np.array([1, 3, 4, 2, 4])
    foo1 = np.multiply(foo, 2)
    return Label(text = f"[color=debf76]{foo} * 2\n{str(foo1)}[/color]", font_size = '25sp', markup = True)

IceCreamApp().run()
