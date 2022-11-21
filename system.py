from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = Tk()
root.geometry("500x300")
root.title("Just my sample system")
root.iconbitmap("images\pathogen_microbe.ico")

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    
    if id == '' or name == '' or phone == '':
        MessageBox.showinfo("Insert Status", "All fields are required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("insert into student values ('"+ id +"','"+ name +"','"+ phone +"')")
        cursor.execute("commit");
        
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert status","Inserted Successfully!");
        con.close();
        print('insert')
        
def delete():
    if(e_id.get() == ''):
        MessageBox.showinfo("Delete status", "ID is compolsary for delete!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("delete from student where id='"+ e_id.get() +"'")
        cursor.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete status","Deleted Successfully!");
        con.close();
        print('delete')
def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    
    if id == '' or name == '' or phone == '':
        MessageBox.showinfo("Update Status", "All fields are required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("update student set name='"+ name +"',phone='"+ phone +"' where id='"+ id +"'")
        cursor.execute("commit");
        
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        MessageBox.showinfo("Update status","Updated Successfully!");
        con.close();
        print('update')
def get():
    if(e_id.get() == ''):
        MessageBox.showinfo("Fetch status", "ID is compolsary for delete!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("select * from student where id='"+ e_id.get() +"'")
        rows = cursor.fetchall()
        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
        con.close();
        print('get')

def show():
    con = mysql.connect(host='localhost', user='root', password='', database='python-tkinter')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    
    for row in rows:
        insertData = str(row[0]) + '. ' + row[1]
        list.insert(list.size()+1, insertData)
    con.close();
    
    
    
id = Label(root, text='Enter ID', font=('bold', 10)).place(x=20, y=30)
name = Label(root, text='Enter Name', font=('bold', 10)).place(x=20, y=60)
phone = Label(root, text='Enter Phone number', font=('bold', 10)).place(x=20, y=90)

e_id = Entry()
e_id.place(x=150, y=30)
 
e_name = Entry()
e_name.place(x=150, y=60)

e_phone = Entry()
e_phone.place(x=150, y=90)


insert = Button(root, text='insert', font=('italic', 10), bg='white', command=insert)
insert.place(x=20, y=140)

delete = Button(root, text='delete', font=('italic', 10), bg='white', command=delete)
delete.place(x=70, y=140)

update = Button(root, text='update', font=('italic', 10), bg='white', command=update)
update.place(x=130, y=140)

get = Button(root, text='get', font=('italic', 10), bg='white', command=get)
get.place(x=190, y=140)

list = Listbox(root)
list.place(x=290, y=30)
show()
root.mainloop()