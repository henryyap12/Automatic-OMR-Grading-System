import kivy
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
import mysql.connector


class StudentInfo(Screen):
    namee = ObjectProperty(None)
    matric = ObjectProperty(None)
    subject = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.matric.text != "" and self.subject.text != "":
            if self.subject != "":
                mydb = mdb.connect(host="localhost", user="root", passwd="", database="test")
                cursor = mydb.cursor()
                sql = "INSERT INTO test2 (stud_name, stud_matric, subject_name) VALUES (%s, %s, %s)"
                val = (self.namee.text, self.matric.text, self.subject.text)
                cursor.execute(sql, val)
                mydb.commit()

                self.reset()

            else:
                invalidForm()
        else:
            invalidForm()

    def reset(self):
        self.namee.text = ""
        self.matric.text = ""
        self.subject.text = ""


class WindowManager(ScreenManager):
    pass

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()



kv = Builder.load_file("my.kv")
sm = WindowManager()
mydb = mdb.connect(host="localhost", user="root", passwd="", database="test")
cursor = mydb.cursor()


screens = [StudentInfo(name="create")]
for screen in screens:
    sm.add_widget(screen)


class MyMainApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
        MyMainApp().run()