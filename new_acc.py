from tkinter import *
import datetime
from tkinter import messagebox
import main
import pymysql.cursors
from PIL import ImageTk, Image


class new:
    def __init__(self, uname):
        self.top = Tk()
        self.top.geometry("820x600+300+100")
        self.top.title("New Account")
        self.top.configure(background="lightblue")
        self.admid = uname

        self.Label = Label(self.top)
        self.Label.place(relx=0.24, rely=0.0, height=82, width=400)
        self.Label.configure(background="lightblue")
        img1 = ImageTk.PhotoImage(Image.open("images/detail.jpg"))
        self.Label.configure(image=img1)

        self.Label1 = Label(self.top)
        self.Label1.place(relx=0.05, rely=0.15, height=31, width=169)
        self.Label1.configure(background="lightblue")

        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Account Number:''')
        self.Label1.configure(width=169)
        self.Label1.config(font=('Arial', 14, 'bold'))

        self.Label2 = Label(self.top)
        self.Label2.place(relx=-0.013, rely=0.22, height=31, width=169)
        self.Label2.configure(background="lightblue")

        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Name:''')
        self.Label2.configure(width=169)
        self.Label2.config(font=('Arial', 14, 'bold'))

        self.Label3 = Label(self.top)
        self.Label3.place(relx=0.001, rely=0.3, height=31, width=169)
        self.Label3.configure(background="lightblue")

        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Address:''')
        self.Label3.configure(width=169)
        self.Label3.config(font=('Arial', 14, 'bold'))

        self.Label4 = Label(self.top)
        self.Label4.place(relx=-0.004, rely=0.38, height=31, width=169)
        self.Label4.configure(background="lightblue")

        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Gender:''')
        self.Label4.configure(width=169)
        self.Label4.config(font=('Arial', 14, 'bold'))

        self.Label5 = Label(self.top)
        self.Label5.place(relx=-0.01, rely=0.46, height=31, width=169)
        self.Label5.configure(background="lightblue")

        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''E-Mail:''')
        self.Label5.configure(width=169)
        self.Label5.config(font=('Arial', 14, 'bold'))

        self.Label6 = Label(self.top)
        self.Label6.place(relx=0.04, rely=0.54, height=31, width=169)
        self.Label6.configure(background="lightblue")

        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Mobile Number:''')
        self.Label6.configure(width=169)
        self.Label6.config(font=('Arial', 14, 'bold'))

        self.Label7 = Label(self.top)
        self.Label7.place(relx=0.028, rely=0.62, height=31, width=169)
        self.Label7.configure(background="lightblue")

        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Father Name:''')
        self.Label7.configure(width=169)
        self.Label7.config(font=('Arial', 14, 'bold'))

        self.Label8 = Label(self.top)
        self.Label8.place(relx=0.029, rely=0.7, height=31, width=169)
        self.Label8.configure(background="lightblue")

        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Mother Name:''')
        self.Label8.configure(width=169)
        self.Label8.config(font=('Arial', 14, 'bold'))

        self.Label9 = Label(self.top)
        self.Label9.place(relx=0.031, rely=0.78, height=31, width=169)
        self.Label9.configure(background="lightblue")

        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Opening Date:''')
        self.Label9.configure(width=169)
        self.Label9.config(font=('Arial', 14, 'bold'))

        self.Label10 = Label(self.top)
        self.Label10.place(relx=0.0, rely=0.86, height=31, width=169)
        self.Label10.configure(background="lightblue")

        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Balance:''')
        self.Label10.configure(width=169)
        self.Label10.config(font=('Arial', 14, 'bold'))

        self.Button1 = Button(self.top, command=self.register)
        self.Button1.place(relx=0.40, rely=0.95, height=24, width=180)
        self.Button1.configure(text='''REGISTER''')
        self.Button1.configure(width=250)

        self.Entry1 = Entry(self.top)
        self.Entry1.place(relx=0.3, rely=0.22, height=20, relwidth=0.21)
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = Entry(self.top)
        self.Entry2.place(relx=0.3, rely=0.3, height=20, relwidth=0.21)
        self.Entry2.configure(font="TkFixedFont")


        self.s1 = StringVar()
        self.s1.set('MALE')
        self.r1 = Radiobutton(self.top, text='Male', variable=self.s1, value='MALE')
        self.r1.place(relx=0.225, rely=0.38, height=20, relwidth=0.21)
        self.r1.config(background='lightblue')

        self.r2 = Radiobutton(self.top, text='Female', variable=self.s1, value='FEMALE')
        self.r2.place(relx=0.4, rely=0.38, height=20, relwidth=0.21)
        self.r2.config(background='lightblue')

        self.r3 = Radiobutton(self.top, text='Others', variable=self.s1, value='OTHERS')
        self.r3.place(relx=0.55, rely=0.38, height=20, relwidth=0.21)
        self.r3.config(background='lightblue')

        self.Entry3 = Entry(self.top)
        self.Entry3.place(relx=0.3, rely=0.46, height=20, relwidth=0.21)
        self.Entry3.configure(font="TkFixedFont")

        self.Entry4 = Entry(self.top)
        self.Entry4.place(relx=0.3, rely=0.54, height=20, relwidth=0.21)
        self.Entry4.configure(font="TkFixedFont")

        self.Entry5 = Entry(self.top)
        self.Entry5.place(relx=0.3, rely=0.62, height=20, relwidth=0.21)
        self.Entry5.configure(font="TkFixedFont")

        self.Entry6 = Entry(self.top)
        self.Entry6.place(relx=0.3, rely=0.7, height=20, relwidth=0.21)
        self.Entry6.configure(font="TkFixedFont")

        self.Entry7 = Entry(self.top)
        self.Entry7.place(relx=0.3, rely=0.86, height=20, relwidth=0.21)
        self.Entry7.configure(font="TkFixedFont")

        self.Entry8 = Entry(self.top)
        self.Entry8.place(relx=0.3, rely=0.15, height=20, relwidth=0.21)
        self.Entry8.configure(font="TkFixedFont")



        self.Label12 = Label(self.top)
        self.Label12.place(relx=0.3, rely=0.78, height=31, width=169)
        self.Label12.configure(background="lightblue")

        odate = datetime.date.today()
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text=odate)
        self.Label12.configure(width=169)
        self.Label12.config(font=('Arial', 14, 'bold'))
        self.generateaccno()





        self.top.mainloop()



    def generateaccno(self):
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        cursor.execute("select ifnull(max(accno),10000000) from tbaccount")
        row = cursor.fetchone()
        acno = row[0]
        acno = acno + 1
        self.Entry8.configure(state='normal')
        self.Entry8.delete(0, END)
        self.Entry8.insert(0, acno)
        self.Entry8.configure(state='disabled')

    def register(self):
        if (
                self.Entry2.get() == "" or self.Entry3.get() == "" or self.Entry5.get() == "" or self.Entry7.get() == "" or self.Entry8.get() == ""):
            messagebox.showerror("Info", "Can't be Empty")
        else:
            try:
                mob = int(self.Entry4.get())
                bal = int(self.Entry7.get())

            except ValueError as e:
                messagebox.showerror("Info", " Mobile No. and  Opening Balance can be Integers Only")
                return
            name = self.Entry1.get()
            add = self.Entry2.get()
            email = self.Entry3.get()
            mob = self.Entry4.get()
            fname = self.Entry5.get()
            mname = self.Entry6.get()
            bal = self.Entry7.get()
            acno = self.Entry8.get()
            odate = self.Label12['text']
            cgen = self.s1.get()


            try:
                con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
                cursor = con.cursor()
                cursor.execute(
                    "insert into tbaccount values(" + acno + ",'" + name + "','" + add + "','" + cgen + "','" + email + "','" + mob + "','" + fname + "','" + mname + "','" + odate + "'," + bal + ")")

                con.commit()
                rows = cursor.rowcount
                if rows > 0:
                    row = cursor.fetchone()
                    self.Entry1.config(state='disabled')
                    self.Entry2.config(state='disabled')
                    self.Entry3.config(state='disabled')
                    self.Entry4.config(state='disabled')
                    self.Entry5.config(state='disabled')
                    self.Entry6.config(state='disabled')
                    self.Entry7.config(state='disabled')
                    self.Entry8.config(state='disabled')
                    messagebox.showinfo('Info', 'Saved')
                    self.top.destroy()
                    m=main.main(self.admid)




                else:
                    messagebox.showinfo('Info', 'Insert Correct Values')
                    self.Entry1.delete(0, END)
                    self.Entry2.delete(0, END)
                    self.Entry3.delete(0, END)
                    self.Entry5.delete(0, END)
                    self.Entry6.delete(0, END)
                    self.Entry7.delete(0, END)
                    self.Entry4.delete(0, END)
                    # self.Entry10.delete(0, END)

            except Exception as e:
                messagebox.showerror("Info :", e)
                return











#obj = new('1')
