import tkinter as tk
from tkinter import messagebox

# Arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't divide by 0"
    return x / y

# Operation dictionary
operation_dict = {
    "Add": add,
    "Subtract": subtract,
    "Multiply": multiply,
    "Divide": divide,
}

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        result = operation_dict[operation](num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Operation dropdown
operation_var = tk.StringVar(root)
operation_var.set("Add")  # default value
tk.Label(root, text="Select operation:").grid(row=2, column=0)
operation_menu = tk.OptionMenu(root, operation_var, *operation_dict.keys())
operation_menu.grid(row=2, column=1)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2)

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Run the app
root.mainloop()
