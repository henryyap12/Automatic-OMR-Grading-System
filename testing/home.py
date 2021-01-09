from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter as tk

try:
    my_connect = mysql.connector.connect(host="localhost", user="root", passwd="", database="automaticomr")
    cur = my_connect.cursor()
except Exception as e:
    print(e)


def login():
    global email
    global login
    global password
    email = emailS.get()
    password = passwordS.get()
    select_sql = ("SELECT * FROM users WHERE email='{}' AND password='{}'".format(email, password))
    mycursor = my_connect.cursor()
    mycursor.execute(select_sql)
    usercheck = mycursor.fetchone()
    if usercheck:
        print("pass")
        login = Toplevel(window)
    else:
        failed()


def reset():
    email.text = ""
    password.text = ""


def failed():
    global failed_message
    failed_message = Toplevel(window)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="black", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="#4ABDAC", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=failed_destroy).pack()


def failed_destroy():
    failed_message.destroy()


def build():
    width = 700
    height = 700
    window = Tk()
    window.call('wm', 'iconphoto', window, tk.PhotoImage(file='logo.png'))
    window.config(bg="#4ABDAC")
    window.title("Automatic OMR Grading System")
    window.geometry("700x700")
    window.minsize(width, height)
    window.maxsize(width=700, height=700)
    return window


window = build()
lb = Label(window, bg="#4ABDAC",  font=('arial', 20, 'bold'), fg="white", text="Automatic OMR Grading System")
lb.place(x=130, y=30)
emailS = StringVar()
passwordS = StringVar()

emailE = Entry(window, relief=FLAT, textvariable=emailS, bg="white")
emailE.place(x=240, y=170, width=200, height=30)

label1 = Label(window, font="40", fg="white", bg="#4ABDAC", text="Email")
label1.place(x=240, y=140, width=200, height=30)

label2 = Label(window, font="40", fg="white", bg="#4ABDAC", text="Password")
label2.place(x=240, y=220, width=200, height=30)

passwordE = Entry(window, show="*", relief=FLAT, textvariable=passwordS, bg="white")
passwordE.place(x=240, y=250, width=200, height=30)


submit = Button(window, activebackground="#87CEEB", text="login", pady=5, padx=20, command=login)
submit.place(x=240, y=350,width=200)

window.mainloop()
