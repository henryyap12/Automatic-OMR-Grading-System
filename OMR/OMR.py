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

# try:
#     con = mdb.connect("localhost", "root", "", "w2")
#     cur = con.cursor()
# except Exception as e:
#     print(e)
#
# class myDatabase:
#     def __init__(self):
#         self.db = mysql.connector.connect(**con)
#         self.c = self.db.cursor()
#
#
#
#
# db_connection = myDatabase()
# db_answer = db_connection.get_rows()


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                mydb = mdb.connect(host="localhost", user="root", passwd="", database="yap")
                cursor = mydb.cursor()
                sql = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
                val = (self.namee.text, self.email.text, self.password.text)
                cursor.execute(sql, val)
                mydb.commit()

                # cursor.execute("INSERT INTO user (fullname, email, password) VALUES (%s, %s, %s)")
                # mydb.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.namee.text = ""
        self.email.text = ""
        self.password.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if mydb.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = mydb.get_user(self.current)
        self.n.text = "Username: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("main.kv")
sm = WindowManager()
mydb = mdb.connect(host="localhost", user="root", passwd="", database="yap")
cursor = mydb.cursor()

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

    sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    MyMainApp().run()
