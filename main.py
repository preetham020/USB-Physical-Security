import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser

root = tk.Tk()
root.title("USB Controller")
root.geometry("400x300")

# Password for enabling/disabling USB ports
password = "snist"

def button2_clicked():
    # Create a password prompt dialog box
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password_label = tk.Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()

    def ok_button_click():
        if password_entry.get() == password:
            command = r'reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v "Start" /t REG_DWORD /d 3 /f >nul'
            subprocess.run(command, shell=True)
            password_window.destroy()
            success_label.config(text="USB Ports Enabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)

    ok_button = tk.Button(password_window, text="OK", command=ok_button_click)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

def button1_clicked():
    # Create a password prompt dialog box 
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password_label = tk.Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()

    def ok_button_click():
        if password_entry.get() == password:
            command = r'reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v "Start" /t REG_DWORD /d 4 /f >nul'
            subprocess.run(command, shell=True)
            password_window.destroy()
            success_label.config(text="USB Ports Disabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)

    ok_button = tk.Button(password_window, text="OK", command=ok_button_click)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

button1 = tk.Button(root, text="Disable USB Ports", command=button1_clicked)
button1.pack()

button2 = tk.Button(root, text="Enable USB Ports", command=button2_clicked)
button2.pack()

success_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2", fg="#00ff00")
success_label.pack()

root.mainloop()
