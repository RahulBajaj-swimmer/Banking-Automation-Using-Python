from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import main

class mod_acc:
    def __init__(self,uname):
        self.rt=Tk()
        self.rt.title("ACCOUNT MODIFY")
        self.rt.configure(background="lightblue")
        self.rt.geometry("820x560+300+175")
        self.admid = uname

        self.l1=Label(self.rt)
        self.l1.place(relx=0.00, rely=0.0, height=120, width=900)
        img1 = ImageTk.PhotoImage(Image.open("images/acmod.gif"))
        self.l1.configure(image=img1,background="lightblue")

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.29, rely=0.37, height=31, width=169)
        self.Label2.configure(background="lightgray")


        self.Label2.configure(text='''ENTER ACCOUNT NUMBER''')
        self.Label2.configure(width=169)

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.499, rely=0.37, height=31, relwidth=0.21)
        self.Entry1.configure(font="TkFixedFont",background="#e0e0d1")
        self.Entry1.insert(0, "1001")
        self.Entry1.configure(state="readonly")
        self.Entry1.configure(state="normal")


        self.Button1 = Button(self.rt,command=self.view) #
        self.Button1.place(relx=0.32, rely=0.59, height=74, width=350)
        self.Button1.configure(text="MODIFY ACCOUNT")
        #self.Button1.configure(width=156)

        self.Frame1 = Frame(self.rt)
        # self.Frame1.place(relx=0.18, rely=0.36, relheight=0.60, relwidth=0.67)
        self.Frame1.configure(relief=FLAT)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="lightcyan")
        self.Frame1.configure(width=525)

        #self.Frame1.place_forget()
        self.rt.mainloop()
    def view(self):
        if (self.Entry1.get() == ""):
            messagebox.showerror("Info", "Can't be Empty")
        else:
            con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
            cursor = con.cursor()
            aid = self.Entry1.get()
            cursor.execute("select * from tbaccount where accno=%s", (aid))
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                row=cursor.fetchone()
                self.Entry1.config(state='disabled')
                self.Frame1.place(relx=0.22, rely=0.44, relheight=0.55, relwidth=0.68)
                self.l2 = Label(self.Frame1)
                self.l2.place(relx=0.32, rely=0.00, height=35, width=258)
                self.l2.configure(background="lightgray")
                self.l2.configure(text='''ENTER UPDATED INFORMATION''')


                self.Label3 = Label(self.Frame1)
                self.Label3.place(relx=0.27, rely=0.18, height=31, width=120)
                self.Label3.configure(background="lightgray")

                self.Label3.configure(text='''NAME''')
                # self.Label3.configure(width=169)

                self.Entry2 = Entry(self.Frame1)
                self.Entry2.place(relx=0.48, rely=0.18, height=31, relwidth=0.21)
                self.Entry2.configure(font="TkFixedFont",background="#e0e0d1")
                self.Entry2.insert(0,row[1])
                self.Entry2.configure(state="readonly")
                self.Entry2.configure(state="normal")

                self.Label4 = Label(self.Frame1)
                self.Label4.place(relx=0.27, rely=0.29, height=31, width=120)
                self.Label4.configure(background="lightgray")

                self.Label4.configure(text='''ADDRESS''')

                self.Entry3 = Entry(self.Frame1)
                self.Entry3.place(relx=0.48, rely=0.29, height=31, relwidth=0.21)
                self.Entry3.configure(font="TkFixedFont",background="#e0e0d1")
                self.Entry3.insert(0, row[2])
                self.Entry3.configure(state="readonly")
                self.Entry3.configure(state="normal")

                self.Label5 = Label(self.Frame1)
                self.Label5.place(relx=0.27, rely=0.40, height=31, width=120)
                self.Label5.configure(background="lightgray")

                self.Label5.configure(text='''E-MAIL''')

                self.Entry4 = Entry(self.Frame1)
                self.Entry4.place(relx=0.48, rely=0.40, height=31, relwidth=0.21)
                self.Entry4.configure(font="TkFixedFont",background="#e0e0d1")
                self.Entry4.insert(0, row[4])
                self.Entry4.configure(state="readonly")
                self.Entry4.configure(state="normal")

                self.Label6 = Label(self.Frame1)
                self.Label6.place(relx=0.27, rely=0.51, height=31, width=120)
                self.Label6.configure(background="lightgray")

                self.Label6.configure(text='''MOBILE NO''')

                self.Entry5 = Entry(self.Frame1)
                self.Entry5.place(relx=0.48, rely=0.51, height=31, relwidth=0.21)
                self.Entry5.configure(font="TkFixedFont",background="#e0e0d1")
                self.Entry5.insert(0, row[5])
                self.Entry5.configure(state="readonly")
                self.Entry5.configure(state="normal")

                self.Button1 = Button(self.Frame1, command=self.update)  #
                self.Button1.place(relx=0.25, rely=0.74, height=65, width=360)
                self.Button1.configure(text="UPDATE")
                #self.Button1.configure(width=156)

            else:
                messagebox.showinfo('Info', 'Invalid Account No.')
                self.Entry1.delete(0, END)


    def update(self):
        if (self.Entry2.get() == "" or self.Entry3.get() == "" or self.Entry4.get() == ""):
            messagebox.showerror("Info", "Can't be Empty")
            #try:
            #    amo = int(self.Entry5.get())
            #except TypeError as e:
             #   messagebox.showerror("Info", "Mobile No can be Integer Only")
              #  return


        else:
            con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
            cursor = con.cursor()
            aid = self.Entry1.get()
            aname = self.Entry2.get()
            add = self.Entry3.get()
            mail = self.Entry4.get()
            mob = self.Entry5.get()
            cursor.execute("update tbaccount set cname=%s, cadd=%s, cemail=%s, cmob=%s  where accno=%s",(aname, add, mail, mob, aid))
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                row = cursor.fetchone()

                self.Entry1.config(state='disabled')
                self.Entry2.config(state='disabled')
                self.Entry3.config(state='disabled')
                self.Entry4.config(state='disabled')
                self.Entry5.config(state='disabled')

                messagebox.showinfo('Info', 'Information Updated')
                self.rt.destroy()
                object = main.main(self.admid)



#obj=mod_acc()