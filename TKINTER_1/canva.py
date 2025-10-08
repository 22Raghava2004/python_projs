from tkinter import *
'''
window = Tk()
window.geometry("700x500")

c = Canvas(window, width=1600, height=600, bg="black")
c.pack()

x1, y1, x2, y2 = 50, 150, 150, 250


for i in range(5):
    c.create_rectangle(x1, y1, x2, y2, width=4, fill="pink", dash=(4,5))
    x1 += 120  # move right
    x2 += 120  

window.mainloop()

'''


window = Tk()
window.geometry("700x500")

c = Canvas(window, width=1600, height=400, bg="black")
c.pack()

x1, y1, x2, y2 = 50, 150, 150, 250

def draw_rect(i, x1, y1, x2, y2):
    if x2<=1600: #i<5:
        c.create_rectangle(x1, y1, x2, y2, width=4, fill="pink",outline="yellow", dash=(4,5))
        window.after(500, draw_rect, i+1, x1+120, y1, x2+120, y2)

draw_rect(0, x1, y1, x2, y2)
window.mainloop()


