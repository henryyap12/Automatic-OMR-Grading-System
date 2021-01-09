from tkinter import *
from tkinter import messagebox
import bcrypt
import mysql.connector


class Login:
    def __init__(self):
        width = 720
        height = 480
        self.loginWindow = Tk()
        self.loginWindow.title("Login")
        self.loginWindow.geometry("720x480")
        self.loginWindow.config(bg="#87CEEB")
        self.loginWindow.minsize(width, height)
        self.loginWindow.maxsize(width=720, height=480)
        self.canvas = Canvas(self.loginWindow, width=300, height=300, bg="white")
        self.canvas.place(x=210, y=80)
        self.label = Label(self.loginWindow, font="40", fg="#87CEEB",bg="white", text="LOGIN")
        self.label.place(x=330, y=90)
        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.usernameE = Entry(self.loginWindow, relief=FLAT, textvariable=self.usernameS, bg="gray")
        self.usernameE.place(x=265, y=170,width=200,height=30)
        self.label1 = Label(self.loginWindow,font="40",fg="white",bg="#87CEEB",text="Username")
        self.label1.place(x=265, y=140,width=200,height=30)
        self.label2 = Label(self.loginWindow, font="40", fg="white", bg="#87CEEB", text="Password")
        self.label2.place(x=265, y=220,width=200,height=30)
        self.passwordE = Entry(self.loginWindow, show="*", relief=FLAT, textvariable=self.passwordS,bg="gray")
        self.passwordE.place(x=265, y=250,width=200,height=30)
        # Actual Variales
        self.username = self.usernameS.get()
        self.password = self.passwordS.get()
        self.submit = Button(self.loginWindow, activebackground="#87CEEB",text="Submit", pady=5, padx=20, command=self.validate)
        self.submit.place(x=320, y=300)

    def validate(self):
        data = ""
        inputData = ""

        try:
            if database.validData(data, inputData):
                messagebox.showinfo("Successful", "Login Was Successful")
            else:
                messagebox.showerror("Error", "Wrong Credentials")
        except IndexError:
            messagebox.showerror("Error", "Wrong Credentials")

    def run(self):
        self.loginWindow.mainloop()
