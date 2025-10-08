
from tkinter import *

window = Tk()
window.title("Example App")
window.geometry("500x400")

label1=Label(window,text=" ")


def butt():
    if button["text"]=="login":
        button.config(text="logged in ",bg="black",fg="red",font=("lucida",20,"bold"))
        label1.config(text="uoy era yag")
        label1.pack()
       
    else:
        button.config(text="login",bg="green",fg="red",font=("lucida",20,"bold"))
        label1.config(text="uoy era yam ")
        label1.pack()


button=Button(window,text="login",bg="green",fg="red",font=("lucida",20,"bold"))
    
button.config(command=butt)

button.pack()
mainloop()