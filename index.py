import tkinter as tk
# Global variable to hold the calculation
calculation = ""

# Function to update the expression in the text field
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the final result
def evaluate_calculation():
    
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Function to clear the text field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Create main window ( User interface )
root = tk.Tk()
root.geometry("300x260")
root.title("Simple Calculator")

# Text field to display input and result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Button field to display buttons
# 2nd Row with four columns having buttons (1,2,3,+)
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 12))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 12))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 12))
btn_3.grid(row=2, column=3)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 12))
btn_plus.grid(row=2, column=4)
#---------------------------------------<>----------------------------------------#
# 3nd Row with four columns having buttons (4,5,6,-)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 12))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 12))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 12))
btn_6.grid(row=3, column=3)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 12))
btn_minus.grid(row=3, column=4)
#---------------------------------------<>----------------------------------------#
# 4nd Row with four columns having buttons (7,8,9,*)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 12))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 12))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 12))
btn_9.grid(row=4, column=3)
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 12))
btn_multiply.grid(row=4, column=4)
#---------------------------------------<>----------------------------------------#
# 5nd Row with four columns having buttons (open"(",0,close")",division)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 12))
btn_open.grid(row=5, column=1)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 12))
btn_0.grid(row=5, column=2)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 12))
btn_close.grid(row=5, column=3)
btn_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 12))
btn_division.grid(row=5, column=4)
#---------------------------------------<>----------------------------------------#
# 6nd Row with 2 columns having buttons (cleaer, result)
# Equal button spans columns 1 and 2 (column=1, columnspan=2)
btn_clear = tk.Button(root, text="C", command=clear_field, width=10, font=("Arial", 12))
btn_clear.grid(row=6, column=1, columnspan=2)

# Clear button spans columns 3 and 4 (column=2, columnspan=2)
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=10, font=("Arial", 12))
btn_equal.grid(row=6, column=3, columnspan=2)

# Run the application
root.mainloop()
