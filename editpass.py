from tkinter import *
from PIL import Image, ImageTk
import pymysql.cursors
from tkinter import messagebox
import main


class Password:
    def __init__(self, uname):
        self.root = Tk()
        self.root.geometry("1145x500+160+100")
        self.root.title('Update Password')
        # self.root.resizable(False,False)
        self.root.configure(background="lightblue")

        self.admid = uname
        self.conn = pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        self.cursor = self.conn.cursor()

        #  i1 = ImageTk.PhotoImage(Image.open("banksimages/23.jpg"))
        # self.Label1 = Label(self.root,image = i1)
        # self.Label1.place(relx = 0.0,rely = 0.0,relwidth = 0.32,relheight = 0.3)

        i2 = ImageTk.PhotoImage(Image.open("images/updatep.gif"))
        self.Label2 = Label(self.root, image=i2)
        self.Label2.place(relx=0.30, rely=0.027, width=500, height=60)
        self.Label2.configure(background="lightblue")

        i21 = ImageTk.PhotoImage(Image.open("images/pup.jpg"))
        self.Label56 = Label(self.root, image=i21)
        self.Label56.place(relx=0.01, rely=0.0, width=200, height=180)

        i22 = ImageTk.PhotoImage(Image.open("images/pup2.jpg"))
        self.Label200 = Label(self.root, image=i22)
        self.Label200.place(relx=0.81, rely=0.0, width=250, height=160)

        self.Label3 = Label(self.root, text="Enter New Password: ", font=('Times New Roman', '14', 'bold'))
        self.Label3.config(background='gray')
        self.Label3.place(relx=0.26, rely=0.43, width=220, height=30)

        self.Entry1 = Entry(self.root, font=('Times New Roman', 12), show='*')
        self.Entry1.place(relx=0.52, rely=0.43,  width=220, height=30)
        self.Entry1.configure(background="#ebebe0")

        self.Label4 = Label(self.root, text="Confirm Password: ", font=("Times New Roman", '14', 'bold'))
        self.Label4.config(background='gray')
        self.Label4.place(relx=0.26, rely=0.56, width=220, height=30)

        self.Entry2 = Entry(self.root, font=('Times New Roman', 12), show='*')
        self.Entry2.place(relx=0.52, rely=0.56, width=220, height=30)
        self.Entry2.configure(background="#ebebe0")

        self.Button1 = Button(self.root)
        self.Button1.config(background='lightgray', command=self.update)
        self.Button1.configure(text="UPDATE")
        self.Button1.place(relx=0.385, rely=0.75, width=220, height=30)

        self.root.mainloop()

    def update(self):
        pwd = self.Entry1.get()
        cpwd = self.Entry2.get()

        if pwd == "" or cpwd == "":
            messagebox.showerror('Info', 'Cannot be empty')

        else:
            if pwd == cpwd:
                self.cursor.execute('update tbadmin set admpwd = %s where admid = %s', (pwd, self.admid))
                self.conn.commit()
                messagebox.showinfo('Info', 'Updated successfully')
                self.root.destroy()
                aj=main.main(self.admid)
            else:
                messagebox.showerror('Info', 'Password and Confirm Password should match!!')
                self.Entry1.delete(0, END)
                self.Entry2.delete(0, END)

#obj = Password('1')