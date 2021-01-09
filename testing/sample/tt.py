from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter as tk
import csv
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from main import omrmarking
import mysql.connector
from datetime import datetime
from tkinter.filedialog import askopenfilename
import cv2


def main():
    root = Tk()
    Button = MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()