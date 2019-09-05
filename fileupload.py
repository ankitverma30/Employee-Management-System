
from tkinter import filedialog
from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

m=tk.Tk()
connection = sqlite3.connect('Studen.db')
print('Database Created Successfully')

TABLE_NAME='FILE'
IMAGE_ID='IMAGE_ID'
IMAGE='IMAGE'
conn = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( "+IMAGE_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + IMAGE+ " BLOB );"

label6 = Label(m, text="Upload Your Marksheet", fg="#0000A0", width="100")
label6.grid(row=1, column=1, padx=(30, 30), pady=(30,30))

if (connection.execute(conn)):
    print("Student Table Created Succesfully")
def selection():
    m.destroy()
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

    label6 = Label(root, text="Thanks Your file has been uploaded", fg="#0000A0", width="100")
    label6.grid(row=1, column=1, padx=(30, 30), pady=(30, 30))

    print (root.filename)
    root.mainloop()
buttonop = tk.Button(m, text="Upload", command=lambda: selection(), bg="#FFC0CB", fg="#0000A0",
                     bd=8)
buttonop.grid(row=2, column=1, padx=(30, 30), pady=(30, 30))
m.mainloop()