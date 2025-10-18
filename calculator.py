# Simple Calculator with GUI
# Built by a beginner data scientist
# This calculator performs basic arithmetic operations with a user interface

import tkinter as tk
from tkinter import messagebox

# My calculation functions
def add_numbers(x, y):
    """Add two numbers together"""
    result = x + y
    return result

def subtract_numbers(x, y):
    """Subtract second number from first"""
    result = x - y
    return result

def multiply_numbers(x, y):
    """Multiply two numbers"""
    result = x * y
    return result

def divide_numbers(x, y):
    """Divide first number by second"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    result = x / y
    return result

# Function to calculate when button is clicked
def do_calculation():
    """This function runs when user clicks Calculate button"""
    try:
        # Get the numbers from input boxes
        number1 = float(entry_num1.get())
        number2 = float(entry_num2.get())
        
        # Get which operation user selected
        selected_operation = operation_choice.get()
        
        # Do the calculation based on selection
        if selected_operation == "Add":
            answer = add_numbers(number1, number2)
            symbol = "+"
        elif selected_operation == "Subtract":
            answer = subtract_numbers(number1, number2)
            symbol = "-"
        elif selected_operation == "Multiply":
            answer = multiply_numbers(number1, number2)
            symbol = "*"
        elif selected_operation == "Divide":
            answer = divide_numbers(number1, number2)
            symbol = "/"
        
        # Show the result
        result_text.set(f"{number1} {symbol} {number2} = {answer}")
        
    except ValueError:
        # Show error if user didn't enter numbers
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# Function to clear everything
def clear_all():
    """Clear all inputs and results"""
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_text.set("Result will appear here")
    operation_choice.set("Add")

# Create the main window
window = tk.Tk()
window.title("My Simple Calculator")
window.geometry("400x350")
window.configure(bg="#f0f0f0")

# Title label
title_label = tk.Label(window, text="Simple Calculator", 
                       font=("Arial", 18, "bold"), 
                       bg="#f0f0f0", fg="#333333")
title_label.pack(pady=10)

# Frame for inputs
input_frame = tk.Frame(window, bg="#f0f0f0")
input_frame.pack(pady=10)

# First number input
label1 = tk.Label(input_frame, text="First Number:", 
                 font=("Arial", 11), bg="#f0f0f0")
label1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_num1 = tk.Entry(input_frame, font=("Arial", 11), width=20)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# Second number input
label2 = tk.Label(input_frame, text="Second Number:", 
                 font=("Arial", 11), bg="#f0f0f0")
label2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry_num2 = tk.Entry(input_frame, font=("Arial", 11), width=20)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Operation selection
label3 = tk.Label(input_frame, text="Operation:", 
                 font=("Arial", 11), bg="#f0f0f0")
label3.grid(row=2, column=0, padx=5, pady=5, sticky="w")

operation_choice = tk.StringVar()
operation_choice.set("Add")  # Default selection

operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_dropdown = tk.OptionMenu(input_frame, operation_choice, *operations)
operation_dropdown.config(font=("Arial", 11), width=17)
operation_dropdown.grid(row=2, column=1, padx=5, pady=5)

# Frame for buttons
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

# Calculate button
calculate_btn = tk.Button(button_frame, text="Calculate", 
                         font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white",
                         width=12, command=do_calculation)
calculate_btn.grid(row=0, column=0, padx=5)

# Clear button
clear_btn = tk.Button(button_frame, text="Clear", 
                     font=("Arial", 12, "bold"),
                     bg="#f44336", fg="white",
                     width=12, command=clear_all)
clear_btn.grid(row=0, column=1, padx=5)

# Result display
result_frame = tk.Frame(window, bg="white", relief=tk.SUNKEN, bd=2)
result_frame.pack(pady=20, padx=20, fill=tk.BOTH)

result_text = tk.StringVar()
result_text.set("Result will appear here")

result_label = tk.Label(result_frame, textvariable=result_text,
                       font=("Arial", 13, "bold"),
                       bg="white", fg="#2196F3",
                       pady=15)
result_label.pack()

# Footer
footer_label = tk.Label(window, text="Made by a beginner MHMSiddiqui 🎓",
                       font=("Arial", 9), bg="#f0f0f0", fg="#666666")
footer_label.pack(side=tk.BOTTOM, pady=5)

# Start the application
window.mainloop()
