import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as MessageBox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import mysql.connector as mysql
from PIL import Image,ImageTk
root = tk.Tk()

root.geometry("650x450")
root.title("Student Admission System")
root.iconbitmap('images\card_employee.ico')
root.resizable(False, False)

fontStyle=['Times',20,'bold']
fontSize=[10,16,18,24,30]
fontWidth=[10,15,18,20,30,40,50]

l1=tk.Label(root,text='Student Admission', font=24, bg='lightgreen')
l1.grid(row=0,column=0,columnspan=7,padx=10,pady=20,sticky='ew')

l2=tk.Label(root,text='Name', font=fontStyle)
l2.grid(row=1,column=0,padx=5,pady=20)
e2=tk.Entry(root,width=fontWidth[2],bg='lightgreen',font=18)
e2.grid(row=1,column=1, columnspan=3,pady=15)

l3=tk.Label(root,text='Class',font=fontStyle)
l3.grid(row=1,column=4,padx=15,pady=10)
my_class=['Five','Four','Five','Six']
cb1=ttk.Combobox(root,values=my_class,width=7)
cb1.grid(row=1,column=5,padx=10,pady=10)
l_msg = tk.Label(root,text='Msg here', bg='lightgreen',font=fontSize[2])
l_msg.grid(row=1,column=6)

l4 =tk.Label(root,text='Gender', font=fontStyle)
l4.grid(row=2,column=0,padx=5,pady=30)

r1_v=tk.StringVar(value='Female')
r1 =tk.Radiobutton(root,text='Male',variable=r1_v,value='Male')
r1.grid(row=2,column=1) 

r2 =tk.Radiobutton(root,text='Female',variable=r1_v,value='Female')
r2.grid(row=2,column=2)

r3 =tk.Radiobutton(root,text='Others',variable=r1_v,value='Others')
r3.grid(row=2,column=3)

l5=tk.Label(root,text='Mark', font=fontStyle)
l5.grid(row=2,column=4,padx=5,pady=10)
e5=tk.Entry(root,width=10,bg='lightgreen')
e5.grid(row=2,column=5,padx=15)

b1=tk.Button(root, text='Upload', command=lambda:my_upload())
b1.grid(row=3,column=2,padx=50)
b2=tk.Button(root, text='Add Data', command=lambda:my_add())
b2.grid(row=3,column=3)

global filename,img
def my_upload():
    global filename,img
    f_types = [('All files', '*.*'),
        ('JPG','*.jpg'),
        ('PNG','*.png')]
    filename=filedialog.askopenfilename(filetypes=f_types)
    img=ImageTk.PhotoImage(file=filename)
    b3=tk.Button(root,image=img)
    b3.grid(row=4,column=1,columnspan=3,pady=20)
    print('Upload File')
def my_add():
    global filename
    flag_validation=True
    my_name=e2.get()
    my_class=cb1.get()
    my_mark=e5.get()
    my_gender=r1_v.get()
    fob=open(filename,'rb')
    fob=fob.read()
    if my_name == '' or my_class == '' or my_mark == '' or my_gender == '':
        MessageBox.showinfo("Warning Form", "Please fill-in the fields!")
    else:        
        con = mysql.connect(host="localhost", user="root", password="", database="student-system")
        cursor = con.cursor()
        cursor.execute("insert into studentblob values ('"+my_name+"','"+my_class+"','"+my_mark+"','"+my_gender+"','"+fob+"')")
        cursor.execute("commit");
        MessageBox.showinfo("Insert status","Inserted Successfully!");
        con.close();
        print('Add Data')
root.mainloop()