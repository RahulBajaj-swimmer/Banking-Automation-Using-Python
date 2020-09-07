from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import main

class mini_stat:
    def __init__(self, m):
        self.rt = Tk()
        self.rt.title("STATEMENT WINDOW")
        self.rt.geometry("1145x500+160+100")
        self.rt.configure(background="lightblue")
        self.l1 = Label(self.rt)
        self.l1.place(relx=0.01, rely=0.0, height=220, width=220)
        img1 = ImageTk.PhotoImage(Image.open("images/stat.jpg"))
        self.l1.configure(image=img1)
        self.admid=m

        self.l12 = Label(self.rt)
        self.l12.place(relx=0.30, rely=0.08, height=57, width=479)
        img12 = ImageTk.PhotoImage(Image.open("images/minstat.gif"))
        self.l12.configure(image=img12, background="lightblue")

        self.l13 = Label(self.rt)
        self.l13.place(relx=0.78, rely=-0.01, height=220, width=250)
        img13 = ImageTk.PhotoImage(Image.open("images/minstats.jpg"))
        self.l13.configure(image=img13,background="lightblue")

        self.Label2 = Label(self.rt)
        self.Label2.place(relx=0.35, rely=0.30, height=31, width=169)
        self.Label2.configure(text='''ENTER ACCOUNT NUMBER''')
        self.Label2.configure(width=178, background="gray")

        self.Entry1 = Entry(self.rt)
        self.Entry1.place(relx=0.50, rely=0.30, height=31, width=178)
        self.Entry1.configure(font="TkFixedFont", background="#ebebe0")
        self.Entry1.insert(0, "10000001")

        self.Button1 = Button(self.rt, command=self.check)
        self.Button1.place(relx=0.43, rely=0.40, height=60, width=206)
        self.Button1.configure(text="SHOW")

        self.fr = Frame(self.rt)
        self.fr.place(relx=0.0, rely=0.0, relheight=0.999, relwidth=1.1)
        self.fr.configure(relief=FLAT)
        self.fr.configure(borderwidth="2")
        self.fr.configure(relief=GROOVE)
        self.fr.configure(background="lightgray")
        self.fr.configure(width=530)

        self.fr.place_forget()

        self.ta = Text(self.fr)
        self.ta.place(relx=0.0, rely=0.0, relheight=0.999, relwidth=1.1)
        self.ta.configure(background="lightgray")

        #self.l1=Label(self.ta)
        #self


        self.Button1 = Button(self.fr, command=self.close)
        self.Button1.place(relx=0.37, rely=0.83, height=40, width=200)
        self.Button1.configure(text="EXIT")


        self.rt.mainloop()

    def check(self):
        con = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor = con.cursor()
        aid = self.Entry1.get()
        cursor.execute("select * from tbtransaction where transsrcaccno=%s", (aid))
        con.commit()
        rows = cursor.rowcount
        #print(rows)
        if rows > 0:
            #row = cursor.fetchone()
            #self.Label4.configure(text=row[0])
            #self.secans = row[1]
            self.Entry1.config(state='disabled')
            self.fr.place(relx=0.22, rely=0.38, relheight=0.6, relwidth=0.65)

            self.l1=Label(self.ta)
            self.l1.configure(text="Trans ID:")
            self.l1.place(relx=0.01, rely=0.01, height=30, width=50)

            self.l1 = Label(self.ta)
            self.l1.configure(text="Src Acc:")
            self.l1.place(relx=0.1, rely=0.01, height=30, width=50)

            self.l1 = Label(self.ta)
            self.l1.configure(text="Dest Acc:")
            self.l1.place(relx=0.23, rely=0.01, height=30, width=50)

            self.l1 = Label(self.ta)
            self.l1.configure(text="Trans Type:")
            self.l1.place(relx=0.33, rely=0.01, height=30, width=60)

            self.l1 = Label(self.ta)
            self.l1.configure(text="Amount:")
            self.l1.place(relx=0.47, rely=0.01, height=30, width=50)

            self.l1 = Label(self.ta)
            self.l1.configure(text="Date:")
            self.l1.place(relx=0.58, rely=0.01, height=30, width=50)

            self.l1 = Label(self.ta)
            self.l1.configure(text="Time:")
            self.l1.place(relx=0.72, rely=0.01, height=30, width=50)

            #print(row)
            msg = ""
            # i=0
            # r=self.cursor.fetchone()
            #print(r)
            for i in cursor:
                self.ta.insert("1.0", "\n")
                self.ta.insert("2.0", "\n")

                msg = msg + "   "+str(i[0]) + '\t' +"  "+ str(i[1]) +"" + '\t' + "    " + str(i[2])+" "+ '\t'+" " + str(i[3])+" " +'\t'+"  "+ str(i[4])+"   " + '\t'+""+str(i[5])+""+ '\t'+"   "+str(i[6]) + '\n'+"\n"

            #print(msg)
            self.ta.insert("4.0", msg)

            self.ta.configure(state="disabled")


        else:
            messagebox.showinfo('Info', 'Invalid Account Number')
            self.Entry1.delete(0, END)
    def close(self):

        self.rt.destroy()
        o1=main.main(self.admid)


#ob = mini_stat('1')