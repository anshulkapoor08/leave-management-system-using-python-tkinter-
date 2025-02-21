import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # type: ignore
import subprocess

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login Successful!")
        root.destroy()  # Close login window
        subprocess.run(["python", "main.py"])  # Open Dashboard
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# Create main window
root = tk.Tk()
root.title("Login System")
root.geometry("800x500")
root.state("normal")



frame = tk.Frame(root, bg="#ffffff", bd=5, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=250)  # 50% of window size

# Load and display icons
user_icon = Image.open("user.png")
user_icon = user_icon.resize((30, 30), Image.LANCZOS)
photo_user = ImageTk.PhotoImage(user_icon)

pass_icon = Image.open("password.png")
pass_icon = pass_icon.resize((30, 30), Image.LANCZOS)
photo_pass = ImageTk.PhotoImage(pass_icon)

# Username Label & Entry
label_user_icon = tk.Label(frame, image=photo_user, bg="#ffffff")
label_user_icon.grid(row=0, column=0, padx=5)

label_user = tk.Label(frame, text="Username:", font=("Arial", 12), bg="#ffffff")
label_user.grid(row=0, column=1, padx=10, pady=10, sticky="w")

entry_username = tk.Entry(frame, font=("Arial", 12))
entry_username.grid(row=0, column=2, padx=10, pady=10)

# Password Label & Entry
label_pass_icon = tk.Label(frame, image=photo_pass, bg="#ffffff")
label_pass_icon.grid(row=1, column=0, padx=5)

label_pass = tk.Label(frame, text="Password:", font=("Arial", 12), bg="#ffffff")
label_pass.grid(row=1, column=1, padx=10, pady=10, sticky="w")

entry_password = tk.Entry(frame, show="*", font=("Arial", 12))
entry_password.grid(row=1, column=2, padx=10, pady=10)

# Login Button
button_login = tk.Button(frame, text="Login", font=("Arial", 12, "bold"), bg="#008CBA", fg="white", 
                         width=15, command=login, relief="raised")
button_login.grid(row=2, column=1, columnspan=2, pady=50)

# Keep image references to prevent garbage collection
label_user_icon.image = photo_user
label_pass_icon.image = photo_pass
root.mainloop()
