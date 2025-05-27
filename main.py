import tkinter
from tkinter import messagebox
import random
import pyperclip

DEFAULT_EMAIL = "sample@gmail.com"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_pass_generate():
    password_entry.delete(0, tkinter.END)
    rand_letters =[random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    rand_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
    rand_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]

    pass_word_list = rand_letters + rand_numbers + rand_symbols

    random.shuffle(pass_word_list)

    rand_output = "".join(pass_word_list)

    password_entry.insert(0, rand_output)
    pyperclip.copy(rand_output)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showerror(title="Empy Fields", message="Please check for empty fields")
    else:
        is_confirmed = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\n\nAdd these login info?")
        if is_confirmed:
            with open("web_data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
lock_image_canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file="logo.png")
lock_image_canvas.create_image(100, 100, image=lock_image)
lock_image_canvas.grid(column=1, row=0)

# Labels
web_label = tkinter.Label(text="Website:")
web_label.grid(column=0,row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
web_entry = tkinter.Entry()
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

email_entry = tkinter.Entry()
email_entry.insert(0,DEFAULT_EMAIL)
email_entry.grid(column=1,row=2, columnspan=2, sticky="ew")

password_entry = tkinter.Entry()
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
generate_pass = tkinter.Button(text="Generate Password", command=random_pass_generate)
generate_pass.grid(column=2, row=3, sticky="ew")

add_button = tkinter.Button(text="Add", command=save_data)
add_button.grid(column=1, row=4, columnspan=3, sticky="ew")
window.mainloop()
