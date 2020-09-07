from tkinter import *
from PIL import Image, ImageTk
import Forgot
import main
import pymysql.cursors
from tkinter import messagebox
class Login_Class:
    def __init__(self):
        self.top = Tk()
        self.top.geometry("791x500+268+88")
        self.top.title("BANKING SOLUTIONS")
        self. top.configure(background="#FFFFCC")
        
        self.Label1 = Label(self.top)
        self.Label1.place(relx=0.05, rely=0.0, height=370, width=720)
        self.Label1.configure(background="#FFFFCC")
        
        img1 = ImageTk.PhotoImage(Image.open("images/banking.jpeg"))
        self.Label1.configure(image=img1)
        
        self.Label2 = Label(self.top)
        self.Label2.place(relx=0.2, rely=0.72, height=31, width=169)
        self.Label2.configure(background="#FFFFCC")
        
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ENTER ADMIN ID''')
        self.Label2.configure(width=169)

        self.Label3 = Label(self.top)
        self.Label3.place(relx=0.21, rely=0.79, height=31, width=164)
        self.Label3.configure(background="#FFFFCC")
        
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''ENTER PASSWORD''')
        self.Label3.configure(width=164)

        self.Entry1 = Entry(self.top)
        self.Entry1.place(relx=0.47, rely=0.73,height=20, relwidth=0.21)
        self.Entry1.configure(font="TkFixedFont")
        
        self.Entry2 = Entry(self.top)
        self.Entry2.place(relx=0.47, rely=0.80,height=20, relwidth=0.21)
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(show="*")

        self.Button1 = Button(self.top, command=self.login)
        self.Button1.place(relx=0.48, rely=0.90, height=24, width=156)
        self.Button1.configure(text='''LOGIN''')
        self.Button1.configure(width=156)

        self.Button2 = Button(self.top,command=self.forgot)
        self.Button2.place(relx=0.23, rely=0.90, height=24, width=167)
        self.Button2.configure(text='''FORGOT PASSWORD''')
        self.Button2.configure(width=167)
        self.top.mainloop()
        
    def login(self):    
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        un = self.Entry1.get()
        pwd = self.Entry2.get()
        cursor.execute("select * from tbadmin where admid=%s and admpwd=%s",(un,pwd))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            messagebox.showinfo('Info', 'Welcome Admin')

            self.top.destroy()
            m = main.main(un)
        else:
            messagebox.showinfo('Info', 'Invalid Name or Password')
            self.Entry1.delete(0,END)
            self.Entry2.delete(0,END)


  

    
    def forgot(self):
        self.top.destroy()    
        f = Forgot.Forgot_Class()


    
#obj = Login_Class()