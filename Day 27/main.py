from tkinter import *


def button_clicked():
    input_data = input.get()
    if input_data == "":
        input_data = "Alwa"
    my_label.config(text=input_data)

window = Tk()
window.title("First Gui Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am the label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
my_label.config(text="New Text")
input = Entry()
#button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button2 = Button(text="New Button")
button2.grid(column=2, row=0)

# Entry
input.grid(column=3, row=2)

window.mainloop()

