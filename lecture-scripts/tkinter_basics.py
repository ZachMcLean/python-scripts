import tkinter as tk
import os

def list_files(directory):
    try:
        files = os.listdir(directory)
        file_list.delete(0, tk.END)
        for file in files:
            file_list.insert(tk.END, file)
    except OSError as e:
        status_label.config(text=f"Error listing files: {e}")

def go_back():
    global current_dir
    current_dir = os.path.dirname(current_dir)
    list_files(current_dir)

def open_directory():
    global current_dir
    global file_list
    selected_index = file_list.curselection()
    if selected_index:
        selected_item = file_list.get(selected_index)
        directory = selected_item
        current_dir = os.path.join(current_dir, directory)
        list_files(current_dir)

def rename_file():
    selected_file = file_list.get(tk.ACTIVE)
    new_name = new_name_entry.get()
    old_path = os.path.join(current_dir, selected_file)
    new_path = os.path.join(current_dir, new_name)
    try:
        os.rename(old_path, new_path)
        list_files(current_dir)
        status_label.config(text="File renamed successfully!")
    except OSError as e:
        status_label.config(text=f"Error renaming file: {e}")

def delete_file():
    selected_file = file_list.get(tk.ACTIVE)
    file_path = os.path.join(current_dir, selected_file)
    try:
        os.remove(file_path)
        list_files(current_dir)
        status_label.config(text="File deleted successfully!")
    except OSError as e:
        status_label.config(text=f"Error deleting file: {e}")

root = tk.Tk()
root.title("File Explorer")

current_dir = os.getcwd()

file_list = tk.Listbox(root)
file_list.pack()

back_button = tk.Button(root, text="Back", command=go_back)
back_button.pack()

open_button = tk.Button(root, text="Open", command=open_directory)
open_button.pack()

new_name_label = tk.Label(root, text="New Name:")
new_name_label.pack()

new_name_entry = tk.Entry(root)
new_name_entry.pack()

rename_button = tk.Button(root, text="Rename", command=rename_file)
rename_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete_file)
delete_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

list_files(current_dir)

root.mainloop()
