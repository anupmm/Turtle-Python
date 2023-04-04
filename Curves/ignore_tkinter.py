from tkinter import *
import tkinter as tk

window = tk.Tk()

# label = tk.Label(
#     text="Hello, Tkinter",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10
# )





# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg='brown',
#     fg="red",
# )

# entry = tk.Entry(fg="yellow", bg="blue", width=50)

# label.pack()
# entry.pack()

toggle_btn = tk.Button(text="Toggle", width=12, relief="raised")
toggle_btn.pack(pady=5)

def toggle():

    if toggle_btn.config('relief')[-1] == 'sunken':
        toggle_btn.config(relief="raised")
    else:
        toggle_btn.config(relief="sunken")

toggle_btn = tk.Button(text="Toggle", width=12, relief="raised", command=toggle)

window.mainloop()


