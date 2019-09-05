import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import ttk
import tkinter.messagebox

xWindow=tk.Tk()
label1 = Label(xWindow, text="Welcome to Employee Managemenet System ", fg="#0000A0", width="100")
label1.grid(row=0, column=2, padx=(30, 30), pady=(30, 0))

connection = sqlite3.connect('Student.db')
print('Database Created Successfully')

radio =IntVar()

radio2 =IntVar()
cursor = connection.cursor()

TABLE_NAME1 = 'student_details'
STUDENT_ID = 'student_id'
STUDENT_NAME = 'student_name'
COURSE_NAME='COURSE_NAME'
STUDENT_ADDRESS='STUDENT_ADDRESS'
STUDENT_ENROLLMENT_NO='STUDENT_ENROLLMENT_NO'
PASSWORD='PASSWORD'
STUDENT_GENDER='GENDER'

TABLE_NAME2='admin_table'
LOGIN='login'
PWD='password'

conn = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME1 + " ( "+STUDENT_ENROLLMENT_NO+" TEXT NOT NULL, "+ STUDENT_GENDER +" TEXT, "+PASSWORD+" TEXT NOT NULL, " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME + " TEXT , " +STUDENT_ADDRESS+" TEXT , " +COURSE_NAME +" TEXT);"

conn2 = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME2 + " ( " + LOGIN  + " TEXT , " + PWD + " TEXT );"
if (connection.execute(conn)):
    print("Student Table Created Succesfully")
if(connection.execute(conn2)):
    print('Admin Table Created Successfully')

conn3="INSERT into "+TABLE_NAME2+" VALUES ('admin','pwd');"
def student():
    mainWindow=tk.Tk()
    label6 = Label(mainWindow, text="Enrollment No", fg="#0000A0", width="100")
    label6.grid(row=0, column=1, padx=(30, 30), pady=(30, 0))

    loginvari = Entry(mainWindow)
    loginvari.grid(row=0, column=2, padx=(30, 30), pady=(30, 0))

    label7 = Label(mainWindow, text="Password", fg="#0000A0", width="100")
    label7.grid(row=1, column=1, padx=(30, 30), pady=(30, 0))

    pwdvar3 = Entry(mainWindow)
    pwdvar3.grid(row=1, column=2, padx=(30, 30), pady=(60, 0))

    def submitstu():
        logie = loginvari.get()
        loginvari.delete(0, END)
        a=''
        b=''


        passw = pwdvar3.get()
        pwdvar3.delete(0, END)
        cursor2=connection.execute("select "+STUDENT_ENROLLMENT_NO+" , "+PASSWORD+"  "+" FROM "+TABLE_NAME1+"  WHERE "+STUDENT_ENROLLMENT_NO+" = '"+logie+"' and "+PASSWORD+" = '"+passw+"';")
        for row in cursor2:
            a=row[0]
            b=row[1]

        if((a==logie)&(b==passw)):
            print('Login Sucessfull')
            global radio
            global radio
            m=tk.Tk()
            def selection():
                print("got some vsalue"+str(radio.get()))
            def selection2():
                print("got some vsalue"+str(radio2.get()))
            labelname = Label(m, text="Enter Your Details", fg="#0000A0", width="100")
            labelname.grid(row=0, column=1,  padx=(30, 30), pady=(30, 0))

            labelame = Label(m, text="Name", fg="#0000A0", width="100")
            labelame.grid(row=1, column=1, padx=(30, 30), pady=(30, 0))

            name = Entry(m)
            name.grid(row=1, column=2, padx=(30, 30), pady=(30, 0))

            label_gen = Label(m, text="Gender", fg="#0000A0", width="100")
            label_gen.grid(row=2, column=1, padx=(30, 30), pady=(30, 0))

            R6 = Radiobutton(m, text="Male", variable=radio2, value=6,
                             command=selection2)
            R6.grid(row=2, column=2, padx=(30, 30), pady=(30, 0))

            R7 = Radiobutton(m, text="Female", variable=radio2, value=7,
                             command=selection2)
            R7.grid(row=3, column=2, padx=(30, 30), pady=(30, 0))

            label_gen = Label(m, text="Select Course", fg="#0000A0", width="100")
            label_gen.grid(row=4, column=1, padx=(30, 30), pady=(30, 0))


            R1 = Radiobutton(m, text="Computer Science", variable=radio, value=1,
                             command=selection)
            R1.grid(row=4, column=2, padx=(30, 30), pady=(30, 0))

            R2 = Radiobutton(m, text="Electrical Engineering", variable=radio, value=2,
                             command=selection)
            R2.grid(row=5, column=2, padx=(30, 30), pady=(30, 0))

            R3 = Radiobutton(m, text="Mechanical Enginnering", variable=radio, value=3,
                             command=selection)
            R3.grid(row=6, column=2, padx=(30, 30), pady=(30, 0))
            R4 = Radiobutton(m, text="Aerospace", variable=radio, value=4,
                             command=selection)
            R4.grid(row=7, column=2, padx=(30, 30), pady=(30, 0))

            R4 = Radiobutton(m, text="APE Gas", variable=radio, value=5,command=selection)
            R4.grid(row=8, column=2, padx=(30, 30), pady=(30, 0))

            label_add = Label(m, text="Address", fg="#0000A0", width="100")
            label_add.grid(row=9, column=1, padx=(30, 30), pady=(30, 0))

            address = Entry(m)
            address.grid(row=9, column=2, padx=(30, 30), pady=(30, 0))
            def submitstu():
                print('record updated')
            buttonop = tk.Button(m, text="Update", command=lambda: submitstu(), bg="#FFC0CB", fg="#0000A0",
                                bd=8)
            buttonop.grid(row=10, column=2, padx=(30, 30), pady=(30, 30))
            m.mainloop()

        else:
            tkinter.messagebox.showinfo('Sorry Password or Id does not exist')

    button5 = tk.Button(mainWindow, text="Submit", command=lambda: submitstu(), bg="#FFC0CB", fg="#0000A0", bd=8)
    button5.grid(row=2, column=1, padx=(30, 30), pady=(30, 30))
    mainWindow.mainloop()
def admin():

    maiWindow=tk.Tk()
    label2 = Label(maiWindow, text="Login", fg="#0000A0", width="100")
    label2.grid(row=0, column=1, padx=(30, 30), pady=(30, 0))

    loginvar = Entry(maiWindow)
    loginvar.grid(row=0, column=2,padx=(30, 30), pady=(30, 0))

    label3 = Label(maiWindow, text="Password", fg="#0000A0", width="100")
    label3.grid(row=1, column=1, padx=(30, 30), pady=(30, 0))

    pwdvar2 = Entry(maiWindow)
    pwdvar2.grid(row=1, column=2,padx=(30, 30), pady=(60, 0))

    def submit2():
        logi= loginvar.get()
        loginvar.delete(0, END)

        passw = pwdvar2.get()
        pwdvar2.delete(0, END)

        if  (logi=='admin')&(passw=='pwd'):
            mWindow=tk.Tk()
            label3 = Label(mWindow, text="Create Student Enrollment No", fg="#0000A0", width="100")
            label3.grid(row=0, column=1, padx=(150, 30), pady=(30, 0))

            label4 = Label(mWindow, text="Student Roll No", fg="#0000A0", width="100")
            label4.grid(row=1, column=1, padx=(30, 30), pady=(30, 0))

            roll = Entry(mWindow)
            roll.grid(row=1, column=2, padx=(30, 30), pady=(30, 0))

            label5 = Label(mWindow, text="Password", fg="#0000A0", width="100")
            label5.grid(row=2, column=1, padx=(30, 30), pady=(30, 0))

            pw=Entry(mWindow)
            pw.grid(row=2, column=2, padx=(30, 30), pady=(30, 0))

            def su():
                rolln=roll.get()
                loginvar.delete(0, END)

                pas = pw.get()
                pw.delete(0, END)

                conn4="INSERT INTO "+TABLE_NAME1+" ( "+STUDENT_ENROLLMENT_NO+" , "+PASSWORD+" ) "+" VALUES ( '"+rolln+"' , '"+pas+"' );"
                if(connection.execute(conn4)):
                    print('Student Enrolled Successfully')
                    tkinter.messagebox.showinfo('Student Enrolled Sucessfully')

            button5=tk.Button(mWindow, text="Submit", command=lambda: su(), bg="#FFC0CB", fg="#0000A0", bd=8)
            button5.grid(row=3, column=2, padx=(30, 30), pady=(30, 120))
            mWindow.mainloop()
        else:
            tkinter.messagebox.showinfo('Sorry Password or Id does not exist')

    button4 = tk.Button(maiWindow, text="Submit", command=lambda: submit2(), bg="#FFC0CB", fg="#0000A0", bd=8)
    button4.grid(row=3, column=1, padx=(30, 30), pady=(30, 30))
    maiWindow.mainloop()
button2 = tk.Button(xWindow, text="Student", command=lambda: student(),height=10,width=50,bg="#FFC0CB",fg="#0000A0",bd=8)
button2.grid(row=1, column=2,padx=(30, 30), pady=(30,30))
button2 = tk.Button(xWindow, text="Admin", command=lambda: admin(),height=10,width=50,bg="#FFC0CB",fg="#0000A0",bd=8)
button2.grid(row=2, column=2,padx=(30, 30), pady=(30,30))

xWindow.mainloop()