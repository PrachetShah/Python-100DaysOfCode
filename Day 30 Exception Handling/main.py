from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

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
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="Light Yellow")

canvas = Canvas(width=200, height=200, bg="Light Yellow", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(50, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

#Labels
website_label = Label(text="Website:", bg="Light Yellow")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="Light Yellow")
email_label.grid(column=0, row=2)

password_label = Label(text="Password", bg="Light Yellow")
password_label.grid(column=0, row=3)

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)

email_entry = Entry(width=41)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "dummy_email@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", bg="white", command=generate_password, width=14)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=38, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", bg="white", width=16, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()