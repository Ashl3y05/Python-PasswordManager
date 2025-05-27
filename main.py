import tkinter
from tkinter import messagebox

DEFAULT_EMAIL = "sample@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

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
generate_pass = tkinter.Button(text="Generate Password")
generate_pass.grid(column=2, row=3, sticky="ew")

add_button = tkinter.Button(text="Add", command=save_data)
add_button.grid(column=1, row=4, columnspan=3, sticky="ew")
window.mainloop()
