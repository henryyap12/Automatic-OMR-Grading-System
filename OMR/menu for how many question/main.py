from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')
# fix the width of the window
Config.set('graphics', 'width', '550')
# fix the height of the window
Config.set('graphics', 'height', '800')

import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import MySQLdb as mdb
from kivy.uix.boxlayout import BoxLayout
import mysql.connector
from kivy.uix.image import Image, AsyncImage
import kivy.uix.button as Button


class Menu(Screen):
    pass


class Question5(Screen):
    pass


class Question10(Screen):
    pass


class Question20(Screen):
    pass


class Question40(Screen):
    pass


class WindowManager(ScreenManager):
    pass


sm = WindowManager()
sm.add_widget(Question5(name='5'))
sm.add_widget(Question10(name='10'))
sm.add_widget(Question20(name='20'))
sm.add_widget(Question40(name='40'))
sm.add_widget(Menu(name='menu'))


class ScreenManagerApp(App):
    def build(self):
        kv = Builder.load_file("choice.kv")
        return kv


if __name__ == '__main__':
    ScreenManagerApp().run()
