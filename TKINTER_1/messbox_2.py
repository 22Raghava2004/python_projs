from tkinter import *

window=Tk()

window.geometry("600x600")

'''
message=Message(window,text="peaton")
message.grid(row=1,column=1)
'''
'''

var=StringVar()
message=Message(window,textvariable= var,relief=RAISED,padx=20,pady=20)
var.set('welcome')
message.pack()



'''
var=StringVar()  #it is stringvar
entry_var=StringVar()  


def insert():
    
    result=entry_var.get()# gets the ddata from the entry tab
    var.set(result) # set the value of the var to  be result


mesa=Message(window,textvariable=var,relief= RAISED,padx=20,pady=20)
entry=Entry(window,textvariable=entry_var)
button=Button(window,text="ok",command=insert)

mesa.pack()
button.pack()
entry.pack()
window.mainloop()