from tkinter import *
import pymysql.cursors
from PIL import Image,ImageTk
from tkinter import messagebox
import Login
class Forgot_Class:
    def __init__(self):
        self.top = Tk()
        self.top.geometry("791x376+268+88")
        self.top.title("BANKING SOLUTIONS")
        self.top.configure(background="#FFFFCC")
        
     
        self.Label1 = Label(self.top)
        self.Label1.place(relx=0.09, rely=0.0, height=66, width=650)
        self.Label1.configure(background="#FFFFCC")
        img1 = ImageTk.PhotoImage(Image.open("images/FORGOT.jpg"))
        self.Label1.configure(image=img1)
        
        self.Label2 = Label(self.top)
        self.Label2.place(relx=0.25, rely=0.40, height=31, width=169)
        self.Label2.configure(background="#FFFFCC")
        self.Label2.configure(text='''ENTER ADMIN ID''')
        self.Label2.configure(width=169)

        self.Entry1 = Entry(self.top)
        self.Entry1.place(relx=0.47, rely=0.41, height=20, relwidth=0.21)
        self.Entry1.configure(background="white")
        
        self.Button1 = Button(self.top,command=self.check)
        self.Button1.place(relx=0.4, rely=0.55, height=24, width=156)
        self.Button1.configure(text='''CHECK''')
        self.Button1.configure(width=156)

        self.Frame1 = Frame(self.top)
        self.Frame1.place(relx=0.18, rely=0.3, relheight=0.65, relwidth=0.67)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#FFFFCC")
        self.Frame1.configure(width=525)
     
        self.Frame1.place_forget()
        
        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.06, rely=0.03, height=21, width=164)
        self.Label3.configure(background="#FFFFCC")
        self.Label3.configure(text='''YOUR SECURITY QUESTION IS''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.44, rely=0.03, height=21, width=234)
        self.Label4.configure(background="#FFFFCC")
        self.Label4.configure(text='''Label''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.07, rely=0.14, height=21, width=146)
        self.Label5.configure(background="#FFFFCC")
        self.Label5.configure(text='''ENTER SECURITY ANSWER''')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.44, rely=0.14,height=20, relwidth=0.31)
        self.Entry2.configure(background="white")
        
        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.08, rely=0.35, relheight=0.59, relwidth=0.9)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#FFFFCC")
        self.Frame2.configure(width=475)
        self.Frame2.place_forget()
        
        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.04, rely=0.1, height=21, width=135)
        self.Label6.configure(background="#FFFFCC")
        self.Label6.configure(text='''ENTER NEW PASSWORD''')

        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0.04, rely=0.34, height=21, width=162)
        self.Label7.configure(background="#FFFFCC")
        self.Label7.configure(text='''ENTER CONFIRM PASSWORD''')

        self.Entry3 = Entry(self.Frame2,show="*")
        self.Entry3.place(relx=0.46, rely=0.1,height=20, relwidth=0.35)
        self.Entry3.configure(background="white")

        self.Entry4 = Entry(self.Frame2, show="*")
        self.Entry4.place(relx=0.46, rely=0.29,height=20, relwidth=0.35)
        self.Entry4.configure(background="white")

        self.Button3 = Button(self.Frame2, command=self.reset)
        self.Button3.place(relx=0.46, rely=0.54, height=24, width=157)
        self.Button3.configure(text='''RESET''')
        self.Button3.configure(width=157)

        self.Button2 = Button(self.Frame1, command=self.verify)
        self.Button2.place(relx=0.44, rely=0.23, height=24, width=157)
        self.Button2.configure(text='''VERIFY''')
        self.Button2.configure(width=157)        
        self.top.mainloop()
        
    def verify(self):
        usrans = self.Entry2.get()
        if(usrans == self.secans):
            self.Frame2.place(relx=0.08, rely=0.35, relheight=0.59, relwidth=0.9)
            self.Entry2.config(state='disabled')
        else:
            messagebox.showinfo('Info', 'Invalid Security Answer')   
                
    def reset(self):
        pwd = self.Entry3.get()
        cpwd = self.Entry4.get()
        if(pwd == cpwd):
         if len(pwd) <= 5:
            messagebox.showerror('Info','Password should be of atleast 6 characters!')
         else:

            con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
            cursor = con.cursor()        
            aid = self.Entry1.get()
            cursor.execute("update tbadmin set admpwd=%s where admid=%s",(pwd,aid))
            con.commit()
            messagebox.showinfo('Info', 'Password updated successfully')  
            self.top.destroy()
            obj = Login.Login_Class()          
        else:
            messagebox.showinfo('Info', 'Password and Confirm Password should match')
            self.Entry3.delete(0,END)
            self.Entry4.delete(0,END)
            
                
    def check(self):
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        aid = self.Entry1.get()
        cursor.execute("select admsecques, admsecans from tbadmin where admid=%s",(aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            row =cursor.fetchone()
            self.Label4.configure(text=row[0])
            self.secans = row[1]
            self.Entry1.config(state='disabled')
            self.Frame1.place(relx=0.18, rely=0.3, relheight=0.65, relwidth=0.67)
        
        else:
            messagebox.showinfo('Info', 'Invalid ID')
            self.Entry1.delete(0,END)
            
#obj = Forgot_Class()