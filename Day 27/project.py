from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(height=100, width=300)
window.config(padx=20, pady=20)
output = 0
KM = 1.609344

def miles_to_km():
    miles = entry.get()
    new_output = round(float(miles) * KM)
    label3.config(text=new_output)

entry = Entry(width=20)
entry.grid(column=1, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=1)
label2 = Label(text="Miles")
label2.grid(column=2, row=0)
label3 = Label(text=output)
label3.grid(column=1, row=1)
label4 = Label(text="Km")
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()