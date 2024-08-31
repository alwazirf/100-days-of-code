from tkinter import *
from tkinter import messagebox
FONT_NAME = "Courier"
from random import randint, choice, shuffle
import json

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
    new_data = {
        website: {
        "email": email,
        "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            # Open the file and read the old data
            with open("./data.json", "r") as df:
                data = json.load(df)
            # Update the old data with the new data
        except FileNotFoundError:
        # Save the updated data back to the file
            with open("./data.json", "w") as df:
                json.dump(new_data, df, indent=4)
        else:
            data.update(new_data)
            with open("./data.json", "w") as df:
                json.dump(data, df, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
            
def find_password():
    try:
        website_key = website_entry.get()
        with open("./data.json", "r") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found.")
    else:
        if website_key in data:
            email = data[website_key]["email"]
            password = data[website_key]["password"]
            messagebox.showinfo(title=f"{website_key}", message=f"Email: {email} \n"
                                f"Password: {password}")
        else:
            if len(website_key) == 0:
                messagebox.showerror(title="Oops", message="Keyword cannot be empty")
            else:
                messagebox.showerror(title="Oops", message=f"No details for {website_key} exist.")
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

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, padx=0, pady=0)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "alwazirf@gmail.com")
# Entry widget
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, padx=0, pady=0)  # No horizontal or vertical padding

# Button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, padx=0, pady=0)
generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2, padx=0, pady=0)
add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()