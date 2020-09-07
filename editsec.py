from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import main

class Security:
    def __init__(self, uname):
        self.root = Tk()
        self.root.geometry('1145x500+160+100')
        self.root.title('Update Security Settings')
        # self.root.resizable(False,False)
        self.root.configure(background="lightblue")

        self.admid = uname
        self.conn = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        self.cursor = self.conn.cursor()

        i0 = ImageTk.PhotoImage(Image.open("images/sec2.gif"))
        self.Label1 = Label(self.root, image=i0)
        self.Label1.place(relx=0.32, rely=0.1, width=520, height=60)
        self.Label1.configure(background="lightblue")

        i1 = ImageTk.PhotoImage(Image.open("images/secu.jpg"))
        self.Label1 = Label(self.root, image=i1)
        self.Label1.place(relx=0.00, rely=0.0, width=250, height=140)

        i2 = ImageTk.PhotoImage(Image.open("images/secu1.jpg"))
        self.Label2 = Label(self.root, image=i2)
        self.Label2.place(relx=0.84, rely=0.00, width=200, height=150)



        self.Label3 = Label(self.root, text="Your Security Question is: ", font=('Times New Roman', '14', 'bold'))
        self.Label3.config(background='gray')
        self.Label3.place(relx=0.25, rely=0.43, width=250, height=30)

        self.Entry1 = Entry(self.root, font=('Times New Roman', 12))
        self.Entry1.place(relx=0.55, rely=0.43, width=220, height=30)
        self.Entry1.configure(background="#ebebe0")

        self.Label4 = Label(self.root, text="Security Answer: ", font=("Times New Roman", '14', 'bold'))
        self.Label4.config(background='gray')
        self.Label4.place(relx=0.25, rely=0.58, width=250, height=30)

        self.Entry2 = Entry(self.root, font=('Times New Roman', 12))
        self.Entry2.place(relx=0.55, rely=0.58, width=220, height=30)
        self.Entry2.configure(background="#ebebe0")

        self.Button1 = Button(self.root)
        self.Button1.config(command=self.update)
        self.Button1.place(relx=0.445, rely=0.8, width=180, height=40)
        self.Button1.configure(text="UPDATE", background="lightgray")

        self.cursor.execute("select admsecques,admsecans from tbadmin where admid = %s", (self.admid))
        row = self.cursor.fetchone()
        self.Entry1.insert(0, row[0])
        self.Entry2.insert(0, row[1])
        self.conn.commit()

        self.root.mainloop()

    def update(self):
        secques = self.Entry1.get()
        secans = self.Entry2.get()

        if secques == "" or secans == "":
            messagebox.showerror('Info', 'Cannot be empty')

        else:
            self.cursor.execute('update tbadmin set admsecques = %s , admsecans = %s where admid = %s',
                                (secques, secans, self.admid))
            self.conn.commit()
            messagebox.showinfo('Info', 'Updated successfully')
            self.root.destroy()
            u=main.main(self.admid)

#obj = Security('2')