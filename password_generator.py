from tkinter import *
from tkinter import messagebox
import random
import json

# Function to generate password
def password_generation():
    try:
        password_length = int(password_length_entry.get())
        if password_length < 8:
            messagebox.showerror("Error", "Password length should be at least 8")
            return
    except ValueError:
        messagebox.showerror("Error", "Password length should be an integer")
        return

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = [random.choice(letters) for _ in range(password_length // 2)]
    password_list += [random.choice(numbers) for _ in range(password_length // 4)]
    password_list += [random.choice(symbols) for _ in range(password_length // 4)]
    password_list += [random.choice(letters) for _ in range(password_length - len(password_list))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_your.delete(0, END)
    password_your.insert(0, password)

# Function to save password
def save():
    websiteentry = website_name.get()
    emailid = email_your.get()
    passwordsave = password_your.get()
    new_data = {
        websiteentry: {
            "email": emailid,
            "password": passwordsave,
        }
    }

    if len(websiteentry) == 0 or len(passwordsave) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you fill the fields")
    else:
        try:
            with open("passwords.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("passwords.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_name.delete(0, END)
            password_your.delete(0, END)

# Function to find password
def find_password():
    websiteentry = website_name.get()
    try:
        with open("passwords.json") as f:
            data = json.load(f)
            if websiteentry in data:
                email = data[websiteentry]["email"]
                password = data[websiteentry]["password"]
                messagebox.showinfo(title=websiteentry, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

# UI Setup
window = Tk()
window.title("My Passwords")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_name = Entry(width=22)
website_name.focus()
website_name.grid(row=1, column=1)

search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_your = Entry(width=40)
email_your.grid(row=2, column=1, columnspan=2)
email_your.insert(0, 'himanshu@gmail.com')

password_length = Label(text="Password Length:")
password_length.grid(row=3, column=0)

password_length_entry = Entry(width=22)
password_length_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", highlightthickness=0, command=password_generation)
generate.grid(row=3, column=2)

password = Label(text="Password:")
password.grid(row=4, column=0)

password_your = Entry(width=22)
password_your.grid(row=4, column=1)

add = Button(text="Add", width=36, command=save)
add.grid(row=5, column=1, columnspan=2)

window.mainloop()
