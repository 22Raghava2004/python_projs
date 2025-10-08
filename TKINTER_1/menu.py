from tkinter import *



window = Tk()

menu=Menu(window)


file=Menu(menu,tearoff=0)
file.add_command(label="New File")
file.add_command(label="Open File")
file.add_separator()
file.add_command(label="Exit",command=window.quit)

edit=Menu(menu,tearoff=0)
edit.add_command(label="Cut")
edit.add_command(label="Copy")

menu.add_cascade(label="Edit",menu=edit)



menu.add_cascade(label="File",menu=file)
window.config(menu=menu)
window.title("My first GUI")
window.geometry("499x399")
window.mainloop()
