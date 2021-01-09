import csv
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

from PIL import ImageTk, Image
import tkinter as tk
from main import omrmarking
import mysql.connector



try:
    my_connect = mysql.connector.connect(host="localhost",user="root",passwd="",database="automaticomr")
    cur = my_connect.cursor()
except Exception as e:
    print(e)


def build():
    window = Tk()
    window.title('Automatic OMR Grading System')
    window.call('wm', 'iconphoto', window, tk.PhotoImage(file='logo.png'))
    window.geometry("900x900")
    window.maxsize(height=900, width=900)
    window.minsize(height=900, width=900)
    window.config(background="white")

    return window


def openfile():
    filename = filedialog.askopenfilename(title='open')
    global path
    path = filename
    return filename


'''def importcsvdata():
    import_file_path = filedialog.askopenfilename()
    global path
    path = import_file_path
    print (path)
    return import_file_path'''


def show(p):
    img = Image.open(p)
    img = img.resize((450, 750))
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.place(x=400, y=150)


def openImg():
    x = openfile()
    show(x)


def getTextInput():
    student = studentlist.get(1.0, tk.END + "-1c")
    lecturer = lecturelist.get(1.0, tk.END + "-1c")
    course = courselist.get(1.0, tk.END + "-1c")
    ans = answerlist.get(1.0, tk.END + "-1c")
    mark = totalmark.get(1.0, tk.END + "-1c")
    s = omrmarking(path, ans, mark, student, lecturer, course)
    resultlabel = Label(window, bg="white", text="Result:")
    resultlabel.place(x=80, y=580)
    noresult = Label(window, bg="white", text=s, fg='green', font=('arial', 20, 'bold'))
    noresult.place(x=80, y=620,width=60)
    sql = "INSERT INTO student (studentId, subjectcode, userid, mark, totalmark) VALUES ('{}','{}','{}','{}','{}')".format(student,
                                                                                                              course,lecturer,s,mark)
    cur.execute(sql)
    my_connect.commit()
    print(cur.rowcount, "record inserted.")
    show("Scanned.jpg")


window = build()
label_file_explorer = Label(window, text="Automatic OMR Grading ", font=('arial', 20, 'bold'),width=60,height=4,bg="#4ABDAC",fg="white")
label_file_explorer.place(x=-60, y=0)

label_file_explorer.option_add('*Font', 'Times 10')
button_explore = Button(window, text="Browse Omr Sheet", command=openImg)
button_explore.place(x=80, y=150, width=140, height=40)

'''button_exit = Button(window, text="Exit", command=window.destroy)
button_exit.place(x=430, y=80, width=140, height=40)'''


''''l = tk.Label(window, bg="white",width=20, text='')
l.place(x=250,y=80)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Labtest',bg="white",variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.place(x=300,y=100)
c2 = tk.Checkbutton(window, text='Midterm',bg="white",variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.place(x=380,y=100)
c3 = tk.Checkbutton(window, text='Final',bg="white",variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.place(x=460,y=100)'''''


labellecture = Label(window, bg="#4ABDAC",fg="white",text="UserId:").place(x=10, y=10)
labelstudent = Label(window, bg="white", text="Insert StudentId").place(x=80, y=200)
labelcourse = Label(window, bg="white", text="Insert Course").place(x=80, y=250)
labelanswer = Label(window, bg="white", text="Insert True Answer").place(x=80, y=300)
labelmark = Label(window, bg="white", text="Insert Total Mark").place(x=80, y=375)

studentlist = tk.Text(window, height=40)
studentlist.place(x=80, y=225, width=120, height=20)

courselist = tk.Text(window, height=40)
courselist.place(x=80, y=275, width=120, height=20)

answerlist = tk.Text(window, height=40)
answerlist.place(x=80, y=325, width=200, height=20)

lecturelist = tk.Text(window, height=40)
lecturelist.place(x=60, y=10, width=60, height=20)

totalmark = tk.Text(window, height=30)
totalmark.place(x=80, y=400, width=120, height=20)

btnRead = tk.Button(window, height=1, width=10, text="Scan", command=getTextInput)
btnRead.place(x=80, y=500, width=140, height=40)

window.mainloop()
