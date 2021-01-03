'''from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter
import os
import sys
import time


def build():
    window = Tk()
    window.title('Automatic OMR Grading System')
    window.geometry("700x700")
    window.maxsize(height=700, width=700)
    window.minsize(height=700, width=700)
    window.config(background="white")

    return window


def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename


def openImg():
    x = openfn()
    img = Image.open(x)
    img = img.resize((300, 500))
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    f = open("omr.txt", "w")
    f.write(x)

    panel.image = img
    panel.place(x=350, y=150)


def CallBack():
    omr = ""
    os.system('python main.py')
    time.sleep(3)

    data = "Score is: " + str(omr)
    msg = tkinter.Message(window, text=data, width=500)
    msg.place(x=80,y=300)


window = build()
label_file_explorer = Label(window, text="Scan OMR ", width=100, height=4)
label_file_explorer.place(x=0, y=0)
button_explore = Button(window, text="Browse Files", command=openImg)
button_explore.place(x=130, y=80, width=140, height=40)
button_scan = Button(window, text=" Scan ", command=CallBack)
button_scan.place(x=80, y=300, width=140, height=40)
button_exit = Button(window, text="Exit", command=window.destroy)
button_exit.place(x=430, y=80, width=140, height=40)

choice = Label(window,bg="white", text="A:0 , B:1 , C:2 , D:3 , E:4").place(x=80, y=150)
labelchoice = Label(window,bg="white",text="Insert True Answer").place(x=80, y=180)
labelmark = Label(window,bg="white",text="Insert Total Mark").place(x=80, y=230)


input_answer = StringVar(window,name="answer")
answer_input = Entry(window,textvariabl=input_answer,bg="light yellow")
answer_input.place(x=80, y=250, width=120, height=20)


input_mark = StringVar(window,name="mark")
mark_input = Entry(window,textvariable=input_mark,bg="light yellow")
mark_input.place(x=80, y=200, width=120, height=20)


scroll_bar = Scrollbar(window)
input_answer.get()
input_mark.get()
scroll_bar.pack(side=RIGHT,fill=Y)
window.mainloop()
'''

###############################################################

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
from main import omrmarking
import mysql.connector
from datetime import datetime
from tkinter.filedialog import askopenfilename
import cv2

try:
    my_connect = mysql.connector.connect(host="localhost",user="root",passwd="",database="automaticomr")
    cur = my_connect.cursor()
except Exception as e:
    print(e)

now = datetime.now()
formatdate = now.strftime('%Y-%m-%d %H-%M-%S')


def build():
    window = Tk()
    window.title('Automatic OMR Grading System')
    window.call('wm', 'iconphoto', window, tk.PhotoImage(file='logo.png'))
    window.geometry("700x700")
    window.maxsize(height=700, width=700)
    window.minsize(height=700, width=700)
    window.config(background="white")

    return window


def openfile():
    filename = filedialog.askopenfilename(title='open')
    global path
    path = filename
    return filename


def show(p):
    img = Image.open(p)
    img = img.resize((300, 500))
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.place(x=350, y=150)


def openImg():
    x = openfile()
    show(x)


def getTextInput():
    student = studentlist.get(1.0, tk.END + "-1c")
    course = courselist.get(1.0, tk.END + "-1c")
    result = answerlist.get(1.0, tk.END + "-1c")
    mark = totalmark.get(1.0, tk.END + "-1c")
    s = omrmarking(path, result, mark)
    resultlabel = Label(window, bg="white", text="Result:")
    resultlabel.place(x=80, y=480)
    noresult = Label(window, bg="white", text=s, fg='green')
    noresult.place(x=80, y=520)
    noresult.option_add('*Font', '12')
    sql = "INSERT INTO student (studentId, subjectcode, mark, totalmark) VALUES ('{}','{}','{}','{}')".format(student, course,s,mark)
    cur.execute(sql)
    my_connect.commit()
    print(cur.rowcount, "record inserted.")
    show("Scanned.jpg")


window = build()
label_file_explorer = Label(window, text="Scan OMR ", width=100, height=4)
label_file_explorer.place(x=0, y=0)

label_file_explorer.option_add('*Font', 'Times 10')
button_explore = Button(window, text="Browse Files", command=openImg)
button_explore.place(x=80, y=80, width=140, height=40)

'''button_exit = Button(window, text="Exit", command=window.destroy)
button_exit.place(x=430, y=80, width=140, height=40)'''

choice = Label(window, bg="white", text=" A:0 , B:1 , C:2 , D:3 , E:4 ").place(x=80, y=150)

labelstudent = Label(window, bg="white", text="Insert StudentId").place(x=80, y=180)
labelcourse = Label(window, bg="white", text="Insert Course").place(x=80, y=230)
labelanswer = Label(window, bg="white", text="Insert True Answer").place(x=80, y=280)
labelmark = Label(window, bg="white", text="Insert Total Mark").place(x=80, y=330)

studentlist = tk.Text(window, height=10)
studentlist.place(x=80, y=205, width=120, height=20)

courselist = tk.Text(window, height=10)
courselist.place(x=80, y=255, width=120, height=20)

answerlist = tk.Text(window, height=10)
answerlist.place(x=80, y=305, width=120, height=20)

totalmark = tk.Text(window, height=10)
totalmark.place(x=80, y=355, width=120, height=20)

btnRead = tk.Button(window, height=1, width=10, text="Scan", command=getTextInput)
btnRead.place(x=80, y=400, width=140, height=40)

window.mainloop()
