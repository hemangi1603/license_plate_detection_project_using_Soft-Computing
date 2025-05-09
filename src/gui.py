import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import threading

process = None  

def run_detection():
    global process
    try:
        process = subprocess.Popen(["python", "detect_plate.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run detection.\n{str(e)}")

def stop_detection():
    global process
    if process:
        process.terminate()
        messagebox.showinfo("Stopped", "Detection has been stopped.")
        process = None

root = tk.Tk()
root.title("License Plate Detection")
root.geometry("400x250")

label = tk.Label(root, text="Click below to start or stop detection!", font=("Arial", 14))
label.pack(pady=20)

start_button = tk.Button(root, text="Start Detection", command=run_detection, font=("Arial", 12), bg="green", fg="white")
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Detection", command=stop_detection, font=("Arial", 12), bg="red", fg="white")
stop_button.pack(pady=10)

root.mainloop()
