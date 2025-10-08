from tkinter import *

window = Tk()
window.title("Example App")
window.geometry("500x400")

check_box1=IntVar() # this is dynamic variable immidiately change the state if the checkbox is clicked
check_box2=IntVar()
check_box3=IntVar()

e1=Entry()
e2=Entry()
e3=Entry()

e1.grid(row=2,column=3)
e2.grid(row=3,column=3)
e3.grid(row=4,column=3)


chk_but1=Checkbutton(window,text="apple",variable=check_box1)
chk_but2=Checkbutton(window,text="mango",variable=check_box2)
chk_but3=Checkbutton(window,text="banana",variable=check_box3)


def butt():
    num1=int(e1.get())
    num2=int(e2.get())
    num3=int(e3.get())
    if button['text']=="ok":
        var=check_box1.get()
        var2=check_box2.get()
        var3=check_box3.get()

        if var==1:

            label=Label(window,text="you boughta apple it is 20 rupees ")
            apple=num1*20

            
        else:
            label=Label(window,text="its is 0")
            apple=0
        label.grid(row=3,column=4)

        if var2==1:
    
            label2=Label(window,text="you boughta apple it is 20 rupees ")
            mango=num2*30
            

            
        else:
            label2=Label(window,text="its is 0")
            mango=0
        label2.grid(row=4,column=4)

        if var3==1:
    
            label3=Label(window,text="you boughta apple it is 20 rupees ")
            banana=num3*40


            
        else:
            label3=Label(window,text="its is 0")
            banana=0
        label3.grid(row=5,column=4)


    total=apple+mango+banana

    label4=Label(window,text=f"the total of apple mango banana is {total}")
    label4.grid(row=5,column=6)


chk_but1.grid(row=1,column=1)
chk_but2.grid(row=2,column=1)
chk_but3.grid(row=3,column=1)


button=Button(window,text="ok",command=butt)
button.grid()
window.mainloop()