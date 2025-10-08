from tkinter import *

window=Tk()
window.title("calculator")
window.geometry("400x300")
label1=Label(text="enter your first number")
e1=Entry(window,width=40,borderwidth=5)
label2=Label(text="enter your second number")
e2=Entry(window,width=40,borderwidth=5)
operation=StringVar(window)
operation.set("select operation")
menu = OptionMenu(window, operation, "Add", "Subtract", "Multiply", "Divide","exit",command=window.quit)
menu.grid(row=3,column=2)



def calc():
    num1=int(e1.get())
    num2=int(e2.get())
    op=operation.get()
    if button["text"]=="calculate":
        if op=="Add":
            result=num1+num2
            label3=Label(text=f"the result is {result}")
            label3.grid(row=4,column=2)
        elif op=="Subtract":
            result=num1-num2
            label3=Label(text=f"the result is {result}")
            label3.grid(row=4,column=2)
        elif op=="Multiply":
            result=num1*num2
            label3=Label(text=f"the result is {result}")
            label3.grid(row=4,column=2)
        elif op=="Divide":
            result=num1/num2
            label3=Label(text=f"the result is {result}")
            label3.grid(row=4,column=2)
        else:
            result="invalid operation"
    else:
        button["text"]="calculated"
    
    

    
    




button2=Button(text=("do you want o exit"))
button2.config(command=window.quit)
button=Button(text="calculate")
label2.grid(row=1,column=0)
e2.grid(row=1,column=2,columnspan=3,padx=10,pady=10)
label1.grid(row=0,column=0)
e1.grid(row=0,column=2,columnspan=3,padx=10,pady=10)
button.grid(row=3,column=3)
button.config(command=calc) 
button2.grid(row=5,column=2)


window.mainloop()