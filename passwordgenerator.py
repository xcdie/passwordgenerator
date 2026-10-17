import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_var.get())
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6 characters.")
            return
        
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy yet!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("380x260")
root.config(bg="#f4f4f9")

tk.Label(root, text="🔐 Secure Password Generator", font=("Arial", 14, "bold"), bg="#f4f4f9").pack(pady=15)

frame = tk.Frame(root, bg="#f4f4f9")
frame.pack(pady=5)

tk.Label(frame, text="Password Length:", font=("Arial", 11), bg="#f4f4f9").pack(side=tk.LEFT, padx=5)
length_var = tk.StringVar(value="12")
tk.Entry(frame, textvariable=length_var, width=5, font=("Arial", 11)).pack(side=tk.LEFT, padx=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#007BFF", fg="white", font=("Arial", 11, "bold"), width=20)
generate_btn.pack(pady=10)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Arial", 12), width=28, justify="center")
result_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#28a745", fg="white", font=("Arial", 10), width=20)
copy_btn.pack(pady=5)

root.mainloop()