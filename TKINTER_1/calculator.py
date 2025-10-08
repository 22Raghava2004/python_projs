from tkinter import *

window=Tk()

window.geometry("600x600")


#entry of the numbers
entry=Entry(window,width=56,borderwidth=5)
entry.place(x=20,y=20)

#Buttons
def click(num):
    result=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(result)+str(num))






b1=Button(window,text="1",width=12,command=lambda:click(1))
b1.place(x=20,y=60)

b2=Button(window,text="2",width=12,command=lambda:click(2))
b2.place(x=140,y=60)

b3=Button(window,text="3",width=12,command=lambda:click(3))
b3.place(x=260,y=60)

b4=Button(window,text="4",width=12,command=lambda:click(4))
b4.place(x=20,y=120)

b5=Button(window,text="5",width=12,command=lambda:click(5))
b5.place(x=140,y=120)

b6=Button(window,text="6",width=12,command=lambda:click(6))
b6.place(x=260,y=120)

b7=Button(window,text="7",width=12,command=lambda:click(7))
b7.place(x=20,y=180)

b8=Button(window,text="8",width=12,command=lambda:click(8))
b8.place(x=140,y=180)

b9=Button(window,text="9",width=12,command=lambda:click(9))
b9.place(x=260,y=180)


b0=Button(window,text="0",width=12,command=lambda:click(0))
b0.place(x=140,y=240)


#operator 
def addi():
    n1=entry.get()
    global math
    math="addition"
    global i
    i=int(n1)
    entry.delete(0,END)

add=Button(window,text="+",width=12,command=addi)
add.place(x=20,y=240)

def subb():
    n1=entry.get()
    global math
    math="subtraction"
    global i
    i=int(n1)
    entry.delete(0,END)

sub=Button(window,text="-",width=12,command=subb)
sub.place(x=140,y=300)


def mull():
    n1=entry.get()
    global math
    math="multiply"
    global i
    i=int(n1)
    entry.delete(0,END)
mul=Button(window,text="*",width=12,command=mull)
mul.place(x=260,y=240)

def divi():
    n1=entry.get()
    global math
    math="divide"
    global i
    i=int(n1)
    entry.delete(0,END)

div=Button(window,text="/",width=12,command=divi)
div.place(x=20,y=300)

def eql():
    n2=entry.get()
    entry.delete(0,END)
    if math=="addition":
        entry.insert(0,i+int(n2))
    elif math=="subtraction":
        entry.insert(0,i-int(n2))
    elif math=="multiply":
        entry.insert(0,i*int(n2))
    elif math=="divide":
        entry.insert(0,i/int(n2))

   

equal=Button(window,text="=",width=12,command=eql)
equal.place(x=260,y=300)

def clr():
    e.delete(0,END)


clear=Button(window,text="clear",width=12,command=clr)
clear.place(x=20,y=360)







#mainloop
window.mainloop()
