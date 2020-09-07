from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import main
import datetime
class with_acc:
    def __init__(self,uname):
        self.rt=Tk()
        self.rt.title("WITHDRAWAL WINDOW")
        self.rt.configure(background="lightblue")
        self.rt.geometry("1145x500+160+100")
        self.admid = uname

        self.l1 = Label(self.rt)
        self.l1.place(relx=0.29, rely=0.1, height=68, width=500)
        img1 = ImageTk.PhotoImage(Image.open("images/withmon.gif"))
        self.l1.configure(image=img1, background="lightblue")

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.3, rely=0.40, height=31, width=169)
        self.Label2.configure(background="gray")

        self.Label2.configure(text='''ENTER ACCOUNT NUMBER''')
        self.Label2.configure(width=169)

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.45, rely=0.4, height=31, width=189)
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.insert(0,"#00000")
        self.Entry1.configure(state="readonly")
        self.Entry1.configure(state="normal")

        self.lab=Label(self.rt)
        self.lab.place(relx=0.01, rely=0.2, height=180, width=280)
        img12 = ImageTk.PhotoImage(Image.open("images/withdraw.jpg"))
        self.lab.configure(image=img12)

        self.lab1 = Label(self.rt)
        self.lab1.place(relx=0.82, rely=0.2, height=220, width=220)
        img13 = ImageTk.PhotoImage(Image.open("images/wnew.jpg"))
        self.lab1.configure(image=img13)

        self.Button1 = Button(self.rt, command=self.check)
        self.Button1.place(relx=0.4, rely=0.58, height=58, width=173)

        self.Button1.configure(text="ENTER", background="lightgray")

        #self.Label3.configure(width=169)

        self.Frame1 = Frame(self.rt)
        self.Frame1.place(relx=0.28, rely=0.3, relheight=0.25, relwidth=0.068)
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
        #self.Entry2.insert(0, "#5896")
        #self.Entry2.configure(state="readonly")
        #self.Entry2.configure(state="normal")

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.01, rely=0.28, height=31, width=178)
        self.Label4.configure(background="gray")

        self.Label4.configure(text='''ENTER WITHDRAWAL AMOUNT''')

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.5, rely=0.28, height=31, width=178)
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.insert(0, "#5896")
        self.Entry3.configure(state="readonly")
        self.Entry3.configure(state="normal")

        self.Butto = Button(self.Frame1, command=self.other)
        self.Butto.place(relx=0.22, rely=0.6, height=58, width=260)

        self.Butto.configure(text="WITHDRAW MONEY", background="gray")


        #self.Button1.configure(width=456)

        self.rt.mainloop()
    def check(self):
        aid=self.Entry1.get()
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        #aid = self.Entry1.get()
        cursor.execute("select balance from tbaccount where accno=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            row = cursor.fetchone()
            print(row)
            self.Entry1.configure(state="disabled")
            self.Frame1.place(relx=0.26, rely=0.3, relheight=0.45, relwidth=0.43)
            self.Entry2.insert(0, row)
            self.Entry2.configure(state="disabled")
        else:
            messagebox.showerror("Info","Enter Correct Account Number")
    def other(self):
        abc = self.Entry3.get()
        aid = self.Entry1.get()
        self.Entry3.configure(state="disabled")
        abc1 = int(abc)
        #aid = self.Entry1.get()
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        # aid = self.Entry1.get()
        cursor.execute("select balance from tbaccount where accno=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        if rows > 0:
            row = cursor.fetchone()
            row1 = int(row[0])
            print(row[0])

            if(abc1 > row1):
                messagebox.showerror("Info", "Insufficient Balance")
                self.Entry3.configure(state="normal")
            elif(abc1 <=0):
                messagebox.showerror("Info", "Enter Amount Greater than Zero")
                self.Entry3.configure(state="normal")
            else:
                con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
                cursor = con.cursor()
                aid = self.Entry1.get()
                avalue=self.Entry3.get()
                abvalue=self.Entry2.get()
                sub=int(abvalue) - int(avalue)
                cursor.execute("update tbaccount set balance=%s where accno=%s", (sub,aid))
                con.commit()
                rows = cursor.rowcount
                if rows > 0:
                    row = cursor.fetchone()
                    messagebox.showinfo("Info", "Successful")
                    #print("s")
                    a1 = datetime.date.today()
                    a2 = datetime.datetime.now().time()
                    a3 = int(self.Entry3.get())
                    aid = int(self.Entry1.get())
                    con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
                    cursor = con.cursor()
                    cursor.execute("select ifnull(max(transid),0) from tbtransaction")
                    con.commit()
                    row = cursor.fetchone()
                    ano = row[0]
                    ano = ano + 1
                    tp = "Withdrawal"
                    con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
                    cursor = con.cursor()
                    cursor.execute("insert into tbtransaction values(%s,%s,%s,%s,%s,%s,%s)",
                                   (ano, aid, aid, tp, a3, a1, a2))
                    con.commit()
                else:
                    messagebox.showerror("Info", "Transaction Failed")
                self.rt.destroy()
                of=main.main(self.admid)


#ob = with_acc('1')




