import numpy as np
import pandas as pd

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.uix.screen import Screen

Window.clearcolor = (255, 255, 255, 1)

class IceCreamApp(App):

  def build(self):
    foo = np.array([1, 3, 4, 2, 4])
    foo1 = np.multiply(foo, 2)
    return Label(text = f"{foo} * 2\n{str(foo1)}", font_size = '25sp', )

IceCreamApp().run()
