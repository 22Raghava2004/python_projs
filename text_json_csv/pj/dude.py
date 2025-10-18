import csv
import os
from tkinter import *

key = 0
data = {}
window = Tk()
window.title("Employee Data Entry")

label = Label(window, text="Enter the number of employees:")
e1 = Entry(window)
label.grid(row=0, column=0)
e1.grid(row=0, column=1)

text = "C:\\Users\\ragha\\OneDrive\\Desktop\\emp.csv"


def create_entries():
    """Create input fields for given number of employees"""
    num = int(e1.get())
    row_start = 2

    labels = ["ID", "Name", "Salary"]
    for i in range(num):
        Label(window, text=f"Employee {i+1}").grid(row=row_start + i, column=0, padx=5, pady=5)

        e2 = Entry(window)
        e3 = Entry(window)
        e4 = Entry(window)

        e2.grid(row=row_start + i, column=1)
        e3.grid(row=row_start + i, column=2)
        e4.grid(row=row_start + i, column=3)

        # store entries in dictionary
        data[i] = (e2, e3, e4)

    Button(window, text="Save to CSV", command=save_to_csv).grid(row=row_start + num + 1, column=1)


def save_to_csv():
    """Save data from entries to CSV"""
    file_exists = os.path.exists(text)
    with open(text, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID", "Name", "Salary"])  # write header if file doesn't exist
        for i, (e2, e3, e4) in data.items():
            writer.writerow([e2.get(), e3.get(), e4.get()])
    Label(window, text="✅ Data saved successfully!", fg="green").grid(row=len(data) + 5, column=1)


Button(window, text="Create Fields", command=create_entries).grid(row=1, column=1, pady=10)

window.mainloop()
