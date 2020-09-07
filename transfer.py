from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import main
import datetime


class trans_acc:
    def __init__(self, uname):
        self.rt = Tk()
        self.rt.title("TRANSFER WINDOW")
        self.rt.geometry("1145x500+160+100")
        self.rt.configure(background="lightblue")
        self.admid= uname

        self.l1 = Label(self.rt)
        self.l1.place(relx=0.0, rely=0.0, height=180, width=350)
        img1 = ImageTk.PhotoImage(Image.open("images/transfer.png"))
        self.l1.configure(image=img1)

        self.l23 = Label(self.rt)
        self.l23.place(relx=0.36, rely=0.1, height=60, width=450)
        img0 = ImageTk.PhotoImage(Image.open("images/transmon.gif"))
        self.l23.configure(image=img0,background="lightblue")

        self.l24 = Label(self.rt)
        self.l24.place(relx=0.8, rely=0.0, height=200, width=250)
        img20 = ImageTk.PhotoImage(Image.open("images/trans1.png"))
        self.l24.configure(image=img20)

        self.al = Label(self.rt)
        self.al.place(relx=0.35, rely=0.3, height=31, width=178)
        self.al.configure(background="lightgray")

        self.al.configure(text='''ENTER SOURCE ACCOUNT''')

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.52, rely=0.3, height=31, width=178)
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.insert(0, "#5896")
        self.Entry1.configure(state="readonly")
        self.Entry1.configure(state="normal")

        self.Button1 = Button(self.rt, command=self.check)
        self.Button1.place(relx=0.43, rely=0.40, height=60, width=206)
        self.Button1.configure(text="ENTER")
        #self.Button1.configure(width=156)

        self.Frame1 = Frame(self.rt)
        self.Frame1.place(relx=0.3, rely=0.38, relheight=0.45, relwidth=0.43)
        self.Frame1.configure(relief=FLAT)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="lightgray")
        self.Frame1.configure(width=530)

        self.Frame1.place_forget()

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.01, rely=0.03, height=31, width=178)
        self.Label3.configure(background="gray")

        self.Label3.configure(text='''CURRENT BALANCE''')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.5, rely=0.03, height=31, width=178)
        self.Entry2.configure(font="TkFixedFont")
        # self.Entry2.insert(0, "#5896")
        #self.Entry2.configure(state="readonly")
        # self.Entry2.configure(state="normal")

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.01, rely=0.24, height=31, width=178)
        self.Label4.configure(background="gray")

        self.Label4.configure(text='''ENTER DESTINATION ACCOUNT''')

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.5, rely=0.24, height=31, width=178)
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.insert(0, "#000")
        self.Entry3.configure(state="readonly")
        self.Entry3.configure(state="normal")

        self.sutto = Button(self.Frame1, command=self.other)
        self.sutto.place(relx=0.22, rely=0.6, height=58, width=270)
        self.sutto.configure(text="ENTER")

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.03, rely=0.28, relheight=0.55, relwidth=0.68)
        self.Frame2.configure(relief=FLAT)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="lightpink")
        self.Frame2.configure(width=530)

        self.Frame2.place_forget()

        self.Label9 = Label(self.Frame2)
        self.Label9.place(relx=0.01, rely=0.2, height=31, width=178)
        self.Label9.configure(background="lightgray")

        self.Label9.configure(text="CURRENT BALANCE")

        self.Entry9 = Entry(self.Frame2)
        self.Entry9.place(relx=0.5, rely=0.2, height=31, width=178)
        self.Entry9.configure(font="TkFixedFont")
        #self.Entry9.insert(0, "#5896")
        #self.Entry9.configure(state="readonly")
        #self.Entry9.configure(state="normal")

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.01, rely=0.4, height=31, width=178)
        self.Label5.configure(background="lightgray")

        self.Label5.configure(text='''ENTER TRANSFER AMOUNT''')

        self.Entry4 = Entry(self.Frame2)
        self.Entry4.place(relx=0.5, rely=0.4, height=31, width=178)
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.insert(0, "#5896")
        self.Entry4.configure(state="readonly")
        self.Entry4.configure(state="normal")

        self.Buttol = Button(self.Frame2, command=self.nextf)
        self.Buttol.place(relx=0.36, rely=0.6, height=58, width=120)
        self.Buttol.configure(text="TRANSFER")

        self.rt.mainloop()

    def check(self):
        aid = self.Entry1.get()
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        # aid = self.Entry1.get()
        cursor.execute("select balance from tbaccount where accno=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            row = cursor.fetchone()
            print(row)
            self.Entry1.configure(state="disabled")
            self.Frame1.place(relx=0.3, rely=0.38, relheight=0.55, relwidth=0.43)
            self.Entry2.insert(0, row[0])
            self.Entry2.configure(state="disabled")
        else:
            messagebox.showerror("Info", "Enter Correct Account Number")

    def other(self):
        aid = self.Entry3.get()
        aid1=self.Entry1.get()
        if(aid==aid1):
            messagebox.showerror("Info", "Enter Correct Account Number")
        else:
            aid = self.Entry3.get()
            con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
            cursor = con.cursor()
        # aid = self.Entry1.get()
            cursor.execute("select balance from tbaccount where accno=%s", (aid))
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                row = cursor.fetchone()
                #print(row)

                self.Entry3.configure(state="disabled")
                self.Frame2.place(relx=0.07, rely=0.35, relheight=0.55, relwidth=0.78)
                #self.Entry2.insert(0, row)
                #self.Entry2.configure(state="disabled")
                self.Entry9.insert(0, row[0])
                self.Entry9.configure(state="disabled")
            else:
                messagebox.showerror("Info","Enter Correct Account Number")
    def nextf(self):
        aid = int(self.Entry2.get())
        am = int(self.Entry4.get())
        asd = int(self.Entry9.get())
        if(am > aid):
            messagebox.showwarning("Info","Enter Valid Amount")

        else:
            sub=(aid) - (am)
            add=(asd) + (am)
            con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
            cursor = con.cursor()
            aid1 = self.Entry1.get()
            cursor.execute("update tbaccount set balance=%s where accno=%s", (sub,aid1))
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                row = cursor.fetchone()
                #print(row[0])
                con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
                cursor = con.cursor()
                aid2 = self.Entry3.get()
                cursor.execute("update tbaccount set balance=%s where accno=%s", (add, aid2))
                con.commit()
                rows=cursor.rowcount
                if rows > 0:
                    messagebox.showinfo("Info","Successful")
                    a1 = datetime.date.today()
                    a2 = datetime.datetime.now().time()
                    con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
                    cursor = con.cursor()
                    cursor.execute("select ifnull(max(transid),0) from tbtransaction")
                    con.commit()
                    row = cursor.fetchone()
                    ano = row[0]
                    ano = ano + 1
                    tp = "Transfer"
                    a3=int(self.Entry4.get())
                    con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
                    cursor = con.cursor()
                    cursor.execute("insert into tbtransaction values(%s,%s,%s,%s,%s,%s,%s)",
                                   (ano, aid1, aid2, tp, a3, a1, a2))
                    con.commit()
                    self.rt.destroy()
                    qw=main.main(self.admid)
                else:
                    messagebox.showerror("Info", "Failure")
            else:
                messagebox.showerror("Info", "Transaction Failed")

#ob = trans_acc('1')