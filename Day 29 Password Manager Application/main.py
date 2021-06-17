from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '@']

    password_letters = [random.choice(letters) for _ in range(random.randint(5, 6))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 3))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 3))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password) == 0:
        messagebox.showinfo(title="Warning",message="Please Don't leave any fields empty")
    else:
        is_okay = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered:\nEmail:{email}"
                                                       f"\nPassword:{password}\nIs it okay to save?")

        if is_okay:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
            # delete 0 to END is used to delete the entry once it is added once ti type again
            website_entry.delete(0,END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=20,bg='Light Yellow')

canvas = Canvas(width=200, height=200,bg="Light Yellow", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(50, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text="Website:", bg="Light Yellow")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="Light Yellow")
email_label.grid(column=0, row=2)

password_label = Label(text="Password",bg="Light Yellow")
password_label.grid(column=0, row=3)

website_entry = Entry(width=41)
website_entry.grid(column=1, row=1,columnspan=2)

email_entry = Entry(width=41)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0, "dummy_email@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command = password_generator, width=14)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add",width=38,bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
