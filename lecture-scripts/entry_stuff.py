import tkinter as tk


root = tk.Tk()

def get_value():
    button_text.append(entry.get())

def display():
    print(button_text)

button_text = []

entry = tk.Entry(root)
entry.grid(row=0, column=0, rowspan=2)
button = tk.Button(root, text="Get Value", command=get_value)
button['bg'] = 'blue'
button.grid(row=0, column=1)

button2 = tk.Button(root, text="Display", command=display)
button2.grid(row=1, column=1)

root.mainloop()