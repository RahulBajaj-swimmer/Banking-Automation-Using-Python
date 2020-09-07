from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import main
class search_acc:
    def __init__(self,uname):
        self.rt=Tk()
        self.rt.title("SEARCH WINDOW")
        self.rt.configure(background="lightblue")
        self.rt.geometry("750x500+310+200")
        self.admid = uname

        self.l1 = Label(self.rt)
        self.l1.place(relx=0.1, rely=0.0, height=92, width=670)
        img1 = ImageTk.PhotoImage(Image.open("images/srchacc.gif"))
        self.l1.configure(image=img1,background="lightblue")

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.23, rely=0.2, height=28, width=189)
        self.Label2.configure(background="lightgray")

        self.Label2.configure(text='''ENTER ACCOUNT NUMBER''')
        self.Label2.configure(width=169)

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.47, rely=0.2, height=28, relwidth=0.23)
        self.Entry1.configure(font="TkFixedFont", background="#e0ebeb")
        self.Entry1.insert(0,"000000000")
        self.Entry1.configure(state="readonly")
        self.Entry1.configure(state="normal")

        self.Button1 = Button(self.rt, command=self.view)
        self.Button1.place(relx=0.35, rely=0.4, height=50, width=240)
        self.Button1.configure(text='''SEARCH''', background="lightgray")


        self.Frame1 = Frame(self.rt)
        #self.Frame1.place(relx=0.18, rely=0.36, relheight=0.60, relwidth=0.67)
        self.Frame1.configure(relief=FLAT)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ccccb3")
        self.Frame1.configure(width=525)

        self.Frame1.place_forget()


        self.rt.mainloop()
    def view(self):#correct this ftn
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        aid = int(self.Entry1.get())
        cursor.execute("select * from tbaccount where accno=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            row = cursor.fetchone()

            self.Entry1.config(state='disabled')
            self.Frame1.place(relx=0.15, rely=0.28, relheight=0.62, relwidth=0.78)
            index=0
            for i in row:
                #print(i)
                #self.Label2.insert(index,i)
                index+=1

            self.l2=Label(self.Frame1)
            self.l2.place(relx=0.26, rely=0.00, height=35, width=220)
            self.l2.configure(background="gray")
            self.l2.configure(text='''SEARCHED INFORMATION''')

            self.Label3 = Label(self.Frame1)
            self.Label3.place(relx=0.12, rely=0.15, height=31, width=160)
            self.Label3.configure(background="lightgray")
            self.Label3.configure(text='''NAME''')
            self.Entry2 = Entry(self.Frame1)
            self.Entry2.place(relx=0.47, rely=0.15, height=31, relwidth=0.27)
            self.Entry2.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry2.insert(0, row[1])
            self.Entry2.configure(state="disabled")
            #self.Label3.configure(width=169)

            #self.vl = Label(self.Frame1)
            #self.vl.place(relx=0.41, rely=0.18, height=31, relwidth=0.21)
            #self.vl.configure(font="TkFixedFont",text=index)
            #self.vl.insert(index,i)

            self.Label4 = Label(self.Frame1)
            self.Label4.place(relx=0.12, rely=0.24, height=31, width=160)
            self.Label4.configure(background="lightgray")
            self.Label4.configure(text='''ADDRESS''')
            self.Entry3 = Entry(self.Frame1)
            self.Entry3.place(relx=0.47, rely=0.24, height=31, relwidth=0.27)
            self.Entry3.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry3.insert(0, row[2])
            self.Entry3.configure(state="disabled")

            self.Label5 = Label(self.Frame1)
            self.Label5.place(relx=0.12, rely=0.33, height=31, width=160)
            self.Label5.configure(background="lightgray")
            self.Label5.configure(text='''GENDER''')
            self.Entry4 = Entry(self.Frame1)
            self.Entry4.place(relx=0.47, rely=0.33, height=31, relwidth=0.27)
            self.Entry4.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry4.insert(0, row[3])
            self.Entry4.configure(state="disabled")

            self.Label6 = Label(self.Frame1)
            self.Label6.place(relx=0.12, rely=0.42, height=31, width=160)
            self.Label6.configure(background="lightgray")
            self.Label6.configure(text='''E-MAIL''')
            self.Entry5 = Entry(self.Frame1)
            self.Entry5.place(relx=0.47, rely=0.42, height=31, relwidth=0.27)
            self.Entry5.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry5.insert(0, row[4])
            self.Entry5.configure(state="disabled")

            self.Label7 = Label(self.Frame1)
            self.Label7.place(relx=0.12, rely=0.51, height=31, width=160)
            self.Label7.configure(background="lightgray")
            self.Label7.configure(text='''MOBILE NO''')
            self.Entry6 = Entry(self.Frame1)
            self.Entry6.place(relx=0.47, rely=0.51, height=31, relwidth=0.27)
            self.Entry6.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry6.insert(0, row[5])
            self.Entry6.configure(state="disabled")

            self.Label8 = Label(self.Frame1)
            self.Label8.place(relx=0.12, rely=0.6, height=31, width=160)
            self.Label8.configure(background="lightgray")
            self.Label8.configure(text='''FATHER NAME''')
            self.Entry7 = Entry(self.Frame1)
            self.Entry7.place(relx=0.47, rely=0.6, height=31, relwidth=0.27)
            self.Entry7.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry7.insert(0, row[6])
            self.Entry7.configure(state="disabled")

            self.Label9 = Label(self.Frame1)
            self.Label9.place(relx=0.12, rely=0.69, height=31, width=160)
            self.Label9.configure(background="lightgray")
            self.Label9.configure(text='''MOTHER NAME''')
            self.Entry8 = Entry(self.Frame1)
            self.Entry8.place(relx=0.47, rely=0.69, height=31, relwidth=0.27)
            self.Entry8.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry8.insert(0, row[7])
            self.Entry8.configure(state="disabled")

            self.Label10 = Label(self.Frame1)
            self.Label10.place(relx=0.12, rely=0.78, height=31, width=160)
            self.Label10.configure(background="lightgray")
            self.Label10.configure(text='''OPENING DATE''')
            self.Entry9 = Entry(self.Frame1)
            self.Entry9.place(relx=0.47, rely=0.78, height=31, relwidth=0.27)
            self.Entry9.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry9.insert(0, row[8])
            self.Entry9.configure(state="disabled")

            self.Label11 = Label(self.Frame1)
            self.Label11.place(relx=0.12, rely=0.87, height=31, width=160)
            self.Label11.configure(background="lightgray")
            self.Label11.configure(text='''BALANCE''')
            self.Entry10 = Entry(self.Frame1)
            self.Entry10.place(relx=0.47, rely=0.87, height=31, relwidth=0.27)
            self.Entry10.configure(font="TkFixedFont", background="#ffffcc")
            self.Entry10.insert(0, row[9])
            self.Entry10.configure(state="disabled")

            self.Button1 = Button(self.rt, command=self.close)
            self.Button1.place(relx=0.43, rely=0.93, height=34, width=116)
            self.Button1.configure(text="CLOSE")
            #self.Button1.configure(width=156)

        else:
            messagebox.showinfo('Info', 'Invalid Account No.')
            self.Entry1.delete(0, END)
    def close(self):
        self.rt.destroy()
        ob = main.main(self.admid)

#ob=search_acc()