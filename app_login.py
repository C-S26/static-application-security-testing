import webbrowser
import os
import tkinter as tk
from tkinter import messagebox

DB_PASSWORD = "653#@PasskeyAdmin"

def validate_login():
    username = entry_user.get()
    password = entry_pass.get()

    # VULNERABILITY: Hardcoded plaintext credentials 
    # Credentials stored directly in code can be exposed via static analysis
    if username == "admin" and password == "SuperSecret123":
        messagebox.showinfo("Success", "Access Granted! Opening Patch Page...")
        open_patch_page()
    else:
        messagebox.showerror("Error", "Access Denied. Invalid credentials.")

def open_patch_page():
    # RELATIVE PATH LOGIC: 
    # Finds the 'patch_mgmt.html' file in the same folder as this script.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "patch_mgmt.html")
    
    if os.path.exists(file_path):
        webbrowser.open(f"file://{file_path}")
    else:
        messagebox.showwarning("Warning", f"File not found. Ensure 'patch_mgmt.html' is in: {base_dir}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Secure Login Portal")
root.geometry("300x200")

tk.Label(root, text="Username:").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack(pady=5)

tk.Button(root, text="Login", command=validate_login).pack(pady=20)

root.mainloop()
