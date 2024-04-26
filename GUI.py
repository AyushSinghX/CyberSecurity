import os
import random
import string
import tkinter as tk
from tkinter import filedialog

def shred_file(file_path):
    try:
        file_path = file_path.strip('"')
        with open(file_path, "rb+") as f:
            file_size = os.path.getsize(file_path)
            random_data = bytearray(os.urandom(file_size))
            for _ in range(3):
                f.seek(0)
                f.write(random_data)
                f.flush()
            f.truncate()
            f.close()
            os.remove(file_path)
            result_label.config(text="File shredded successfully.")
    except FileNotFoundError:
        result_label.config(text="Error: File not found.")
    except PermissionError:
        result_label.config(text="Error: Permission denied. Make sure the file is not being used by another process.")
    except Exception as e:
        result_label.config(text="Error shredding file: " + str(e))

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

root = tk.Tk()
root.title("File Shredder")

file_label = tk.Label(root, text="Select a file to shred:")
file_label.pack(pady=10)

file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

shred_button = tk.Button(root, text="Shred File", command=lambda: shred_file(file_entry.get()))
shred_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
