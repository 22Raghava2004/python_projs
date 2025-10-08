from tkinter import *

window = Tk()
window.title("Example App")
window.geometry("500x400")

laboon=Label(window, text="Enter your name:",bg="yellow",fg="black",font=("arial",15,"bold"))

label1=Label(window,text="Name",bg="purple",fg="white",font=("arial",15,"bold"))

label2=Label(window,text="bambam",bg="red",fg="white",font=("arial",15,"bold"))

laboon.pack(side=TOP,fill=X,expand=False)
label1.pack(side=LEFT,fill=Y,expand=False)
label2.pack(side=BOTTOM,fill=X,expand=False)



window.mainloop()