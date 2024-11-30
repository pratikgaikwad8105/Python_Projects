import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['Reg No'])
    e2.insert(0,select['Student Name'])
    e3.insert(0,select['Mobile'])
    e4.insert(0,select['Fee'])


def Add():
    Reg_id = e1.get()
    studname = e2.get()
    Mobile = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pratik@8105",
        database="registation")
    mycursor = mysqldb.cursor()

    try:
       sql = "INSERT INTO  registation (id,empname,mobile,salary) VALUES (%s, %s, %s, %s)"
       val = (Reg_id,studname,Mobile,feee)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Student inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Pratik@8105", database="registation")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  registation set empname= %s,mobile= %s,salary= %s where id= %s"
       val = (studname, coursename, feee, studid)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updated successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    studid = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="Pratik@8105",database="registation")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from registation where id = %s"
       val = (studid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleted successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def show():
        global records
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Pratik@8105",database="registation")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,empname,mobile,salary FROM registation")
        records = mycursor.fetchall()
        print(records)
        for row in listBox.get_children():
            listBox.delete(row)

        for i, (id,stname, course,fee) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, stname, course, fee))
            mysqldb.close()


def refresh():

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))

    show()


root = Tk()
root.title("Bus Registration")
root.geometry("825x500")
root.resizable(False, False)

global e1
global e2
global e3
global e4

tk.Label(root, text="Bus Registration", fg="white", background="black", font=("courier", 25, "bold"), border=10).place(x=370, y=45)

tk.Label(root, text="Reg ID").place(x=40, y=10)
Label(root, text="Student Name").place(x=40, y=40)
Label(root, text="Mobile").place(x=40, y=70)
Label(root, text="Fee").place(x=40, y=100)

e1 = Entry(root)
e1.place(x=150, y=10)

e2 = Entry(root)
e2.place(x=150, y=40)

e3 = Entry(root)
e3.place(x=150, y=70)

e4 = Entry(root)
e4.place(x=150, y=100)

Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="Update", command=update, height=3, width=13).place(x=140, y=130)
Button(root, text="Delete", command=delete, height=3, width=13).place(x=250, y=130)
Button(root, text="Refresh", command=refresh, height=3, width=13).place(x=360, y=130)

cols = ('Reg No', 'Student Name', 'Mobile', 'Fee')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col, anchor="center")
    listBox.column(col, anchor=CENTER)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
