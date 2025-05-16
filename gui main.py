

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("Garbage and Spit Detection ")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"g2.webp")
bg.resize((1300,600),Image.LANCZOS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="Garbage and Spit Detection ",width=50,background="#B0E0E6",foreground="white",height=2,font=("Times new roman",19,"bold"))
w.place(x=400,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="black")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


# wlcm=tk.Label(root,text="......Garbage and Spit Detection ......",width=95,height=3,background="#B0E0E6",foreground="white",font=("Times new roman",22,"bold"))
# wlcm.place(x=0,y=620)


frame = tk.LabelFrame(root, text="", width=300, height=250, bd=10, font=('times', 14, ' bold '),bg="#5d5b58")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=10, y=200)

d2=tk.Button(frame,text="Login",command=Login,width=9,height=2,bd=0,background="#B0E0E6",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=90,y=50)


d3=tk.Button(frame,text="Register",command=Register,width=9,height=2,bd=0,background="#B0E0E6",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=90,y=120)



root.mainloop()
