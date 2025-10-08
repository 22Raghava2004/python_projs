from tkinter import *
#import packagee messagebox
import tkinter.messagebox

window=Tk()
#mess=tkinter.messagebox

#mess.showinfo("Information","This is a information message box")
#mess.showwarning("Warning","This is a warning message box")
tkinter.messagebox.showerror("Error","This is a error message box") 



question=tkinter.messagebox.askyesno("weather","will it rain today?")
#question =tkinter.messagebox.askokcancel("weather ","will it rain")
if question ==True:
    tkinter.messagebox.showinfo("yes","tke the rain coat")
else:
    tkinter.messagebox.showinfo("no","no need to take rain coat")
    
    
    
    

question1=tkinter.messagebox.askquestion("weather","will it rain")

if question== True:
    tkinter.messagebox.showwarning("yes","take rain coat")
else:   
    tkinter.messagebox.showwarning("no","no need to take rain coat")
        


mainloop()