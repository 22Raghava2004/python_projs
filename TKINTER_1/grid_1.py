from tkinter import *

window = Tk()
window.title("Example App")
window.geometry("500x400")

laboon=Label(window, text="Enter your name:")

label1=Label(window,text="Name")

e1=Entry(window,width=20, borderwidth=5)
e2=Entry(window,width=20, borderwidth=5)

laboon.grid(row=0,column=1)
label1.grid(row=2,column=1)


e1.grid(row=0,column =2)
e2.grid(row=2,column=2)
window.mainloop()