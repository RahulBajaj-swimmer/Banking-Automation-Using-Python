from tkinter import *
from PIL import Image, ImageTk
import main

class about_us:
    def __init__(self,uname):
        self.root1 = Tk()
        self.root1.geometry("1145x900+160+100")
        self.root1.title('Banking Solutions')
        # self.root1.resizable(False,False)
        self.root1.configure(background="lightblue")
        self.admid=uname

        i1 = ImageTk.PhotoImage(Image.open("images/crb.jpg"))
        self.Label1 = Label(self.root1, image=i1)
        self.Label1.place(relx=0.0, rely=0.0, width=310, height=160)

        i2 =ImageTk.PhotoImage(Image.open("images/auh.jpg"))
        self.Label2 = Label(self.root1, image=i2)
        self.Label2.place(relx=0.79, rely=0.0, width=270, height=162)

        i3 = ImageTk.PhotoImage(Image.open("images/cbh2.png"))
        self.Label3 = Label(self.root1, image=i3)
        self.Label3.place(relx=0.34, rely=0.0, width=470, height=265)

        self.Text1 = Text(self.root1, width=80, height=15, wrap='word')

        self.Text1.place(relx=0.34, rely=0.37) #replace file
        self.Text1.insert('1.0', '''This project has been developed by RAHUL BAJAJ under the supreme
guidance of Er. PUNEET AGGARWAL.
In recent years, The Banking Industry has been undergoing drastic changes, reflecting a number of
underlying developments. Core Banking Solution (CBS) is networking of branches, which enables
Customers to operate their accounts, and avail banking services from any branch of the Bank on
CBS network, regardless of where he maintains his account. The customer is no more the customer
of a Branch. He becomes the Bank's Customer. Thus CBS is a step towards enhancing customer
convenience through anywhere and anytime Banking.

Minimum Software Requirements:

1. Operation System : Windows
2. Language : PYTHON 3.6
3. Front End: PyCharm IDE
4. Back End: MySQL Server 5.0''')
        self.Text1.config(state='disabled', font=('Times New Roman', '12', 'italic'), background="lightgray")
        self.Text2 = Text(self.root1, width=40, height=15, wrap='word')

        self.Text2.place(relx=0.03, rely=0.37)  # replace file
        self.Text2.insert('1.0', '''CONTACT DETAILS:
        
1. MOB:  +919356661112
2. email:  rahulbajaj2233@gmail.com
3. Postal Address:  Guru Ram Dass Nagar, Fzr
4. Pin Code:  152002''')
        self.Text2.config(state='disabled', font=('Times New Roman', '12', 'italic'), background="lightgray")

        self.b = Button(self.root1, command=self.back)
        self.b.place(relx=0.47, rely=0.73, width=200, height=68)
        self.b.configure(text="CLOSE",background="gray")

        self.root1.mainloop()
    def back(self):
        self.root1.destroy()
        zx=main.main(self.admid)


#obj = about_us(1)