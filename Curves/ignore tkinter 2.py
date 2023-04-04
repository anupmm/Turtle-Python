from tkinter import *
from tkinter import ttk
import tkinter as tk

def get_inputs():
    label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
    )
    # curve_type = curve_var.get()
    # if curve_type == 'c':
    #     steps_var.update(36)
    #     # steps_var.delete(0, END)  # Clear the current value of steps
    #     # steps_var.insert(0, 36)  # Set the value of steps to 36
    # else:
    #     steps = int(steps_var.get())
    # iterations = int(iter_var.get())
    # print(f"Curve Type: {curve_type}, Iterations: {iterations}, Steps: {steps}")
    # # Do something with the inputs, e.g. draw the curve using turtle

root = tk.Tk()

# Curve type label and option menu
curve_label = tk.Label(root, text="Curve Type:")
curve_label.grid(row=0, column=0)
curve_var = tk.StringVar(root, value="c")
curve_options = ["c", "s", "a"]
curve_menu = tk.OptionMenu(root, curve_var, *curve_options)
curve_menu.grid(row=0, column=1)

# Iterations label and entry
iter_label = tk.Label(root, text="Iterations:")
iter_label.grid(row=1, column=0)
iter_var = tk.Entry(root)
iter_var.grid(row=1, column=1)

# Steps label and entry
steps_label = tk.Label(root, text="Steps:")
steps_label.grid(row=2, column=0)
steps_var = tk.Entry(root)
steps_var.grid(row=2, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_inputs)
submit_button.grid(row=3, column=1)

root.mainloop()
