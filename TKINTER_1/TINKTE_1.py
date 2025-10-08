# import tkinter 
#gui interaction 
#adding inputs
# main loop

'''

import tkinter as tk
window=tk.Tk()

lab=tk.Label(window,text="Hello World")
jb=tk.Button(window,text="Click Me")

jb.pack()
lab.pack()

window.mainloop()
'''
# or
'''
 
from tkinter import *

window = Tk()
window.title("Example App")
window.geometry("300x200")

lab = Label(window, text="Enter your name:")
lab.pack()

entry = Entry(window) # input field
entry.pack()

def greet():
    name = entry.get()
    
    if name=="kushal":
        print(lab.config(text=f"Hello, {name}!you are gay"))
    else:
        print(lab.config(text=f"Hello, {name}!"))

btn = Button(window, text="Greet Me", command=greet)
btn.pack()

window.mainloop()

'''
 
from tkinter import *
window=Tk()

window.title("My first GUI")
window.geometry("499x399")
window.config(bg="green",padx=20,pady=23)

#giving objects to class
lab=Label(window,bg="black",fg="red",text="my name is raghav",font=("arial",20,"bold"),padx=10,pady=25)
text=Text(window,height=5,width=20)

frame1=Frame(window,bg="blue",height=100,width=100)
frame1.pack()
frame2=Frame(window,bg="red",height=100,width=100)
frame2.pack()
def duck():
    if button["text"]=="click me":

        button.config(text="clicked")
        window2=Toplevel(window)
        window2.title("win2")
        window2.geometry("400x300")
        text2=text.get("1.0","end-1c")
        lab2=Label(window2,bg="black",fg="red",font=("arial",20,"bold"),padx=10,pady=25,text=text2)
        lab2.pack()
        window2.mainloop()
        
    else:
        button.config(text="click me")

button=Button(window,text="click me",bg="dark blue",fg="red",padx=20,pady=25)

lab.pack()
text.pack()
button.pack()
button.config(command=duck)
window.mainloop()