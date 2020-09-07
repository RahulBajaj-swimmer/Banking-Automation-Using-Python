from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import modify
import new_acc
import delete
import viewacc
import search
import withdraw
import deposit
import transfer
import Mini
import editprof
import editpass
import editsec
import Login
import about

class main:
    def __init__(self, id):
        self.admid  = id
        self.top = Tk()
        self.top.geometry("820x600+300+100")
        self.top.title("BANKING SOLUTIONS")
        self.top.configure(background="lightblue")
        self.top.option_add('*tearOff', False)

        self.Label1 = Label(self.top)
        self.Label1.place(relx=-0.25, rely=-0.24, height=900, width=1230)
        self.Label1.configure(background="lightblue")

        img1 = ImageTk.PhotoImage(Image.open("images/bank2.jpg"))
        self.Label1.configure(image=img1)

        self.mb = Menu(self.top)
        self.top.config(menu=self.mb)

        self.ac = Menu(self.mb)
        self.tr = Menu(self.mb)
        self.ad = Menu(self.mb)
        self.he = Menu(self.mb)

        self.mb.add_cascade(menu=self.ac, label='Account', underline=10)
        self.mb.add_cascade(menu=self.tr, label='Transaction', underline=10)
        self.mb.add_cascade(menu=self.ad, label='Admin', underline=10)
        self.mb.add_cascade(menu=self.he, label='Help', underline=10)

        self.ac.add_command(label="Open New Account", command=lambda: self.new())
        self.ac.add_command(label="Modify Account", command=lambda: self.mod())
        self.ac.add_command(label="Delete Account", command=lambda: self.delete())
        self.ac.add_command(label="View all Accounts", command=lambda: self.view())
        self.ac.add_command(label="Search", command=lambda: self.srch())

        #self.ac.entryconfig('Open New Account', accelerator='Ctrl+N')
        #self.top.bind_all('<Control-n>', self.new)

        self.tr.add_command(label="Withdraw", command=lambda: self.withdraw())
        self.tr.add_command(label="Deposit", command=lambda: self.deposit())
        self.tr.add_command(label="Transfer", command=lambda: self.transfer())
        self.tr.add_command(label="Mini Statement", command=lambda: self.mini())

        self.ad.add_command(label="Edit Profile", command=lambda: self.eprofile())
        self.ad.add_command(label="Edit Password", command=lambda: self.epass())
        self.ad.add_command(label="Edit Security Settings", command=lambda: self.esecurity())
        self.ad.add_command(label="Logout", command=lambda: self.logout())

        self.he.add_command(label="About Us", command=lambda: self.abtus())


        self.top.mainloop()

    def new(self):
        self.top.destroy()
        n = new_acc.new(self.admid)

    def mod(self):
        self.top.destroy()
        m= modify.mod_acc(self.admid)

    def delete(self):
        self.top.destroy()
        d=delete.del_acc(self.admid)

    def view(self):
        self.top.destroy()
        v=viewacc.ViewAllAccount(self.admid)

    def srch(self):
        self.top.destroy()
        s=search.search_acc(self.admid)

    def withdraw(self):
        self.top.destroy()
        w=withdraw.with_acc(self.admid)

    def deposit(self):
        self.top.destroy()
        d=deposit.depo_acc(self.admid)

    def transfer(self):
        self.top.destroy()
        t=transfer.trans_acc(self.admid)

    def mini(self):
        self.top.destroy()
        m=Mini.mini_stat(self.admid)

    def eprofile(self):
        self.top.destroy()
        e=editprof.EditPrf(self.admid)

    def epass(self):
        self.top.destroy()
        ep=editpass.Password(self.admid)

    def esecurity(self):
        self.top.destroy()
        es=editsec.Security(self.admid)

    def logout(self):
        messagebox.showinfo("Warning", "Click Ok to LOGOUT")
        self.top.destroy()
        m=Login.Login_Class()

    def abtus(self):
        self.top.destroy()
        a=about.about_us(self.admid)



#obj=main('1')