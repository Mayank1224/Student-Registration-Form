import tkinter as tk 
from tkinter import * 

root=tk.Tk()   

root.title('Student Registration form for college')

root.geometry('700x550+400+400')   

root.configure(bg='#9ED8FC')

l1=Label(master=root,text='First Name', width=10, height=2, bg='black',fg='white',
        font='timesnewroman 16 bold', bd=2, relief='ridge')
l1.grid(row=0,column=0)   

l2=Label(master=root,text='Last Name', width=10, height=2, bg='black',fg='white',       
        font='timesnewroman 16 bold', bd=2, relief='ridge')
l2.grid(row=1,column=0)  

l3=Label(master=root,text='Branch', width=10, height=2, bg='black',fg='white',
        font='timesnewroman 16 bold', bd=2, relief='ridge')
l3.grid(row=2,column=0)   

l4=Label(master=root,text='Address', width=10, height=2, bg='black',fg='white',
        font='timesnewroman 16 bold', bd=2, relief='ridge')
l4.grid(row=3,column=0)  
l6=Label(master=root,text='Contact no', width=10, height=2, bg='black',fg='white',
        font='timesnewroman 16 bold', bd=2, relief='ridge')
l6.grid(row=4,column=0)
l8=Label(master=root,text='10th %age', width=10, height=2, bg='black',fg='white',
        font='timesnewroman 16 bold', bd=2, relief='ridge')
l8.grid(row=5,column=0)
l8=Label(master=root,text='12th %age', width=10, height=2, bg='black',fg='white',
        font='timesnewroman 16 bold', bd=2, relief='ridge')
l8.grid(row=6,column=0)
l9=Label(master=root,text='Email', width=10, height=2, bg='black',fg='white',
        font='timesnewroman 16 bold', bd=2, relief='ridge')
l9.grid(row=7,column=0)


l5=Label(root,bg='#9ED8FC',font='arial 14')
l5.grid(row=8, column=1)

def submit():
    first_name=StringVar()
    Last_name=StringVar()
    branch=StringVar()
    address=StringVar()
    contact_no=int()
    Tenth_percentage = int()
    Twelfth_percentage = int()
    Email = StringVar()

    first_name=e1.get()
    Last_name=e2.get()
    branch=e3.get()
    address=e4.get()
    contact_no=e5.get()
    Tenth_percentage=e7.get()
    Twelfth_percentage=e8.get()
    Email=e9.get()

    import mysql.connector
    connection=mysql.connector.connect(host='localhost',username='root', password='yourpassword', 
                               database='your_database_name')
    # table create
    create_query='''create table  if not exists details 
                    (first_name text,Last_name varchar(10),branch text,address text,contact_no long,Tenth_percentage int,Twelfth_percentage int, email varchar(100));'''
    insert_query='''insert into details(first_name,Last_name,branch,address,contact_no,Tenth_percentage,Twelfth_percentage,email) 
                        values(%s,%s,%s,%s,%s,%s,%s,%s);'''
    cursor=connection.cursor()
    cursor.execute(create_query)
    cursor.execute(insert_query,(first_name,Last_name,branch,address,contact_no,Tenth_percentage,Twelfth_percentage,Email))
    connection.commit() 

    print(first_name)
    print(Last_name)
    print(branch)
    print(address)
    print(contact_no)
    print(Tenth_percentage)
    print(Twelfth_percentage)
    print(Email)
 
b1=Button(master=root,text='Submit', width=10, height=2, bg='#313EF5',fg='white',
        font='timesnewroman 16 bold', bd=2, relief='ridge', command=submit)
b1.grid(row=10,column=1)

e1=Entry(root,bd=3, width=30, font='arial 18')
e1.grid(row=0,column=1)

e2=Entry(root,bd=3, width=30, font='arial 18')
e2.grid(row=1,column=1)

e3=Entry(root,bd=3, width=30, font='arial 18')
e3.grid(row=2,column=1)

e4=Entry(root,bd=3, width=30, font='arial 18')
e4.grid(row=3,column=1)

e5=Entry(root,bd=3, width=30, font='arial 18')
e5.grid(row=4,column=1)

e7=Entry(root,bd=3, width=30, font='arial 18')
e7.grid(row=5,column=1)

e8=Entry(root,bd=3, width=30, font='arial 18')
e8.grid(row=6,column=1)

e9=Entry(root,bd=3, width=30, font='arial 18')
e9.grid(row=7,column=1)

root.mainloop()
