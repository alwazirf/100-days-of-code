from tkinter import *
from tkinter import messagebox
FONT_NAME = "Courier"
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = (
        [choice(letters) for _ in range(randint(8,10))] +
        [choice(symbols) for _ in range(randint(2,4))] +
        [choice(numbers) for _ in range(randint(2,4))]
    )
    shuffle(password)

    newPassword = "".join(password)
    password_entry.insert(0, newPassword)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askyesnocancel(title=website, message=f"There are the details entered: \nEmail: {email}"
                                f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("./data.txt", "a") as df:
                df.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "alwazirf@gmail.com")
# Entry widget
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, padx=0, pady=0)  # No horizontal or vertical padding

# Button
generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2, padx=0, pady=0)
add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()