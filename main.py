from tkinter import *

window = Tk()
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
window.title("Mile to KM Converter")


def calculate_miles():
    convert = int(miles.get()) * 1.689
    output.config(text=convert)


miles = Entry(width=10)
miles.grid(column=2, row=1)

label_mile = Label(text="Mile")
label_mile.grid(column=3, row=1)

label_2 = Label(text="is equal to")
label_2.grid(column=1, row=2)

output = Label(text=" ")
output.grid(column=2, row=2)

km_label = Label(text="KM")
km_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate", command=calculate_miles)
calculate_button.grid(column=2, row=3)

window.mainloop()
