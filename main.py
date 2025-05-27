import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
lock_image_canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file="logo.png")
lock_image_canvas.create_image(100, 100, image=lock_image)
lock_image_canvas.grid(column=1, row=0)

# Labels
web_label = tkinter.Label(text="Website:")
web_label.grid(column=0,row=1,)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
web_entry = tkinter.Entry(width=45)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")

email_entry = tkinter.Entry(width=45)
email_entry.grid(column=1,row=2, columnspan=2, sticky="w")

password_entry = tkinter.Entry(width=28)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
generate_pass = tkinter.Button(text="Generate Password")
generate_pass.grid(column=2, row=3, sticky="w")

add_button = tkinter.Button(text="Add", width=38)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")
window.mainloop()
