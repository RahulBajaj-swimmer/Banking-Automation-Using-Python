from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Progressbar
import threading
import Login

import time
class Loading_class:
    def __init__(self):
        self.top = Tk()
        self.top.geometry("791x376+268+88")
        self.top.title("BANKING SOLUTIONS")
        self. top.configure(background="#FFFFCC")
        
        self.Label1 = Label(self.top)
        self.Label1.place(relx=0.24, rely=0.0, height=82, width=443)
        self.Label1.configure(background="#FFFFCC")
        img1 = ImageTk.PhotoImage(Image.open("images/rahul2.jpg"))
        self.Label1.configure(image=img1)
        
        self.v1 = IntVar()  #it will hold the current value of progress bar
        
        self.Label2 = Label(self.top)
        self.Label2.place(relx=0.08, rely=0.43, height=41, width=374)
        self.Label2.configure(background="#FFFFCC")
        self.Label2.configure(width=374)       
        
        
        self.pb = Progressbar(self.top,orient=HORIZONTAL)
        self.pb.config(mode='determinate',maximum=100)
        self.pb.config(variable=self.v1)
        
        self.pb.place(relx=0.08, rely=0.56, relwidth=0.87 , relheight=0.0, height=22)
        self.pb.configure(length="690")
        tup = (101,)   
        self.t1 = threading.Thread(target=self.move, args = tup , name='first' )
        self.t1.start()
        self.top.after(500, self.check)
        self.top.mainloop()
        
        
    def move(self,a):
        for i in range(a):
            self.v1.set( i) 
            self.Label2.configure(text='LOADING '+str(self.v1.get()) +'%')            
            time.sleep(.05)
       
    def check(self):
        if self.v1.get()!=100:
            self.top.after(500, self.check)
        else:
            self.top.destroy()
            o1 = Login.Login_Class()
    
                
#obj = Loading_class()