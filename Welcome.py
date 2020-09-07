from tkinter import *
from PIL import Image,ImageTk
import Loading

class welcome_class:
    def __init__(self):
        self.top = Tk()
        self.top.geometry("791x390+268+88")
        self.top.title("BANKING SOLUTIONS")
        self. top.configure(background="lightblue")
        self.Label1 = Label(self.top)
        self.Label1.place(relx=-0.12, rely=-0.03, height=321, width=1004)
        img1 = ImageTk.PhotoImage(Image.open("images/corebanking1.jpg"))
        self.Label1.configure(image=img1)

        self.Button1 = Button(self.top, command=self.click)
        self.Button1.place(relx=0.39, rely=0.83, height=44, width=205)
        self.Button1.configure(text='''CLICK HERE TO CONTINUE''')
        self.top.mainloop()
        
    def click(self):
        self.top.destroy()
        l = Loading.Loading_class()
        

if __name__ == '__main__':
    obj = welcome_class()
    