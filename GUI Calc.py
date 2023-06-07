"""
nnnhhh002 2023/06/06

Watching a YT video and trying to learn how to make a calculator with a simple
GUI overlay

YT VIDEO: https://www.youtube.com/watch?v=NzSCNjn4_RI&ab_channel=NeuralNine

"""
import tkinter as tk

calculation = ""


# Allows button inputs to be interpreted
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")  # Delete button
    text_result.insert(1.0, calculation)


# Takes the numbers given to calculation and evals
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


# Function for clearing result window
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


"""
Add History Button Option
Allows user to see last 10 previous answer results
"""

# The beginning of graphics
root = tk.Tk()
"""
Where the graphics are
"""
# This Size of the window for application
root.geometry("300x275")
# Where the text and numbers will enter Creating a small window and column
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
# The size of the text field
text_result.grid(columnspan=5)
# One Button
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
btn_1.grid(row=2, column=1)
# Two Button
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 15))
btn_2.grid(row=2, column=2)
# Three Button
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 15))
btn_3.grid(row=2, column=3)
# Four Button
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 15))
btn_4.grid(row=3, column=1)
# Five Button
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 15))
btn_5.grid(row=3, column=2)
# Six Button
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 15))
btn_6.grid(row=3, column=3)
# Seven Button
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 15))
btn_7.grid(row=4, column=1)
# Eight Button
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 15))
btn_8.grid(row=4, column=2)
# Nine Button
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 15))
btn_9.grid(row=4, column=3)
# Zero Button
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 15))
btn_0.grid(row=5, column=2)
# Addition Button
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 15))
btn_plus.grid(row=2, column=4)
# Subtraction Button
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 15))
btn_minus.grid(row=3, column=4)
# Multiplication Button
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 15))
btn_mul.grid(row=4, column=4)
# Division Button
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 15))
btn_div.grid(row=5, column=4)
# Allows for parentheses
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 15))
btn_open.grid(row=5, column=1)
# Close parentheses
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 15))
btn_close.grid(row=5, column=3)
# Clear button
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 15))
btn_clear.grid(row=6, column=1, columnspan=2)
# Equal Button
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 15))
btn_equals.grid(row=6, column=3, columnspan=2)
# The ending of graphics
root.mainloop()
