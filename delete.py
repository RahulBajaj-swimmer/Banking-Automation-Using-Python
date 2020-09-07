from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import main
class del_acc:
    def __init__(self,uname):
        self.rt=Tk()
        self.rt.title("DELETION WINDOW")
        self.rt.configure(background="lightblue")
        self.rt.geometry("750x500+310+200")
        self.admid = uname

        self.l1 = Label(self.rt)
        self.l1.place(relx=0.1, rely=0.0, height=170, width=700)
        img1 = ImageTk.PhotoImage(Image.open("images/delacc.gif"))
        self.l1.configure(image=img1, background="lightblue")

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.3, rely=0.40, height=40, width=169)
        self.Label2.configure(background="lightgray")

        self.Label2.configure(text='''ENTER ACCOUNT NUMBER''')
        #self.Label2.configure(width=169)

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.53, rely=0.40, height=40, relwidth=0.21)
        self.Entry1.configure(font="TkFixedFont", background="#ffffff")
        self.Entry1.insert(0,"10000001")

        self.Entry1.configure(state="normal")


        self.Button1 = Button(self.rt, command=self.view)
        self.Button1.place(relx=0.36, rely=0.60, height=50, width=200)
        self.Button1.configure(text="DELETE ACCOUNT")
        #self.Button1.configure(width=156)

        self.rt.mainloop()

    def view(self):
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        aid = int(self.Entry1.get())
        cursor.execute("select * from tbaccount where accno=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:

            messagebox.showwarning("Warning", "Delete Account")
            con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
            cursor = con.cursor()
            aid = int(self.Entry1.get())
            cursor.execute("delete from tbaccount where accno=%s", (aid))
            con.commit()

            messagebox.showinfo('Info', 'Account Deleted')
            self.rt.destroy()
            obs = main.main(self.admid)


        else:
            messagebox.showinfo('Info', 'Invalid Account No.')
            self.Entry1.delete(0, END)



#ab=del_acc(1)