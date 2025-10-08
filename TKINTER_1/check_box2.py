from tkinter import *

window = Tk()
window.title("Example App")
window.geometry("500x400")

# Variables
check_box1 = IntVar()
check_box2 = IntVar()
check_box3 = IntVar()

# Entries
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e1.grid(row=2, column=2)
e2.grid(row=3, column=2)
e3.grid(row=4, column=2)

# Checkbuttons
chk_but1 = Checkbutton(window, text="apple", variable=check_box1)
chk_but2 = Checkbutton(window, text="mango", variable=check_box2)
chk_but3 = Checkbutton(window, text="banana", variable=check_box3)
chk_but1.grid(row=2, column=1)
chk_but2.grid(row=3, column=1)
chk_but3.grid(row=4, column=1)

# Labels aligned with entries
label1 = Label(window, text="")
label2 = Label(window, text="")
label3 = Label(window, text="")
label_total = Label(window, text="")
label1.grid(row=2, column=3, padx=10)  # same row as e1
label2.grid(row=3, column=3, padx=10)  # same row as e2
label3.grid(row=4, column=3, padx=10)  # same row as e3
label_total.grid(row=5, column=2, columnspan=2)

# Button
def butt():
    try:
        num1 = int(e1.get())
    except:
        num1 = 0
    try:
        num2 = int(e2.get())
    except:
        num2 = 0
    try:
        num3 = int(e3.get())
    except:
        num3 = 0

    # Apple
    apple = num1 * 20 if check_box1.get() == 1 else 0
    label1.config(text=f"Apple: {apple} rupees" if apple else "Apple not bought")

    # Mango
    mango = num2 * 30 if check_box2.get() == 1 else 0
    label2.config(text=f"Mango: {mango} rupees" if mango else "Mango not bought")

    # Banana
    banana = num3 * 40 if check_box3.get() == 1 else 0
    label3.config(text=f"Banana: {banana} rupees" if banana else "Banana not bought")

    # Total
    total = apple + mango + banana
    label_total.config(text=f"Total: {total} rupees")

button = Button(window, text="ok", command=butt)
button.grid(row=6, column=2, pady=10)

window.mainloop()
