import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(plen=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    s = ''
    if use_lowercase:
        s += string.ascii_lowercase
    if use_uppercase:
        s += string.ascii_uppercase
    if use_digits:
        s += string.digits
    if use_special:
        s += string.punctuation
    
    if not s:
        raise ValueError("No character set selected for password generation")

    return ''.join(random.sample(s, plen))

def generate_and_show_password():
    plen = int(length_entry.get())
    use_lowercase = lowercase_var.get() == 1
    use_uppercase = uppercase_var.get() == 1
    use_digits = digits_var.get() == 1
    use_special = special_var.get() == 1

    try:
        password = generate_password(plen, use_lowercase, use_uppercase, use_digits, use_special)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(fg="#007bff")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def animate_button(button):
    button.config(bg="#0056b3", activebackground="#004080", relief="sunken")
    root.after(100, lambda: button.config(bg="#007bff", activebackground="#0056b3", relief="raised"))

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0", bd=0)
frame.pack(padx=20, pady=20)

title_label = tk.Label(frame, text="Password Generator", font=("Helvetica", 20), bg="#f0f0f0")
title_label.grid(row=0, columnspan=2, pady=10)

length_label = tk.Label(frame, text="Password Length:", bg="#f0f0f0")
length_label.grid(row=1, column=0, sticky="w")

length_entry = tk.Entry(frame)
length_entry.grid(row=1, column=1)

lowercase_var = tk.IntVar()
lowercase_checkbox = tk.Checkbutton(frame, text="Include Lowercase", variable=lowercase_var, bg="#f0f0f0", bd=0)
lowercase_checkbox.grid(row=2, column=0, columnspan=2, sticky="w")

uppercase_var = tk.IntVar()
uppercase_checkbox = tk.Checkbutton(frame, text="Include Uppercase", variable=uppercase_var, bg="#f0f0f0", bd=0)
uppercase_checkbox.grid(row=3, column=0, columnspan=2, sticky="w")

digits_var = tk.IntVar()
digits_checkbox = tk.Checkbutton(frame, text="Include Digits", variable=digits_var, bg="#f0f0f0", bd=0)
digits_checkbox.grid(row=4, column=0, columnspan=2, sticky="w")

special_var = tk.IntVar()
special_checkbox = tk.Checkbutton(frame, text="Include Special Characters", variable=special_var, bg="#f0f0f0", bd=0)
special_checkbox.grid(row=5, column=0, columnspan=2, sticky="w")

generate_button = tk.Button(frame, text="Generate Password", command=lambda: [generate_and_show_password(), animate_button(generate_button)], bg="#007bff", fg="white", relief="raised")
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

password_label = tk.Label(frame, text="Generated Password:", bg="#f0f0f0")
password_label.grid(row=7, column=0, columnspan=2, sticky="w")

password_entry = tk.Entry(frame, bg="#ffffff", bd=0)
password_entry.grid(row=8, column=0, columnspan=2, pady=5)

root.mainloop()
