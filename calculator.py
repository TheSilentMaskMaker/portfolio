# Import the tkinter library for GUI
import tkinter as tk

# Define the Calculator class
class Calculator:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Calculator")
        
        # Initialize expressions
        self.total_expression = ""
        self.current_expression = ""
        
        # Create display frame
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        
        # Define digit and operation mappings
        self.digits = {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            0: (4, 0), '.': (4, 1)
        }
        
        self.operations = {
            "/": "\u00F7",
            "*": "\u00D7",
            "-": "-",
            "+": "+"
        }
        
        # Create button frames and buttons
        self.buttons_frame = self.create_buttons_frame()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        
        # Bind keyboard keys
        self.bind_keys()
        
    # Define function to bind keys
    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.evaluate())
        self.root.bind("<KP_Enter>", lambda event: self.evaluate())
        for key in self.digits:
            self.root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.root.bind(key, lambda event, operator=key: self.append_operator(operator))
    
    # Create display labels
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#F3F3F3", fg="#25265E", padx=24, font=("Arial", 16))
        total_label.pack(expand=True, fill='both')
        
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#F3F3F3", fg="#25265E", padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill='both')
        
        return total_label, label

    # Create display frame
    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg="#F3F3F3")
        frame.pack(expand=True, fill="both")
        return frame

    # Update expression functions
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    # Create buttons for digits and operators
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="#FFF", fg="#25265E", font=("Arial", 24, "bold"), borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="#F8FAFF", fg="#25265E", font=("Arial", 20), borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=3, sticky=tk.NSEW)
            i += 1

    # Create special buttons
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="#F8FAFF", fg="#25265E", font=("Arial", 20), borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#CCEDFF", fg="#25265E", font=("Arial", 20), borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=2, columnspan=2, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="#F8FAFF", fg="#25265E", font=("Arial", 20), borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg="#F8FAFF", fg="#25265E", font=("Arial", 20), borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=0, sticky=tk.NSEW)

    # Define special functionality
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    # Create buttons frame
    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        for x in range(5):
            frame.rowconfigure(x, weight=1)
            frame.columnconfigure(x, weight=1)
        return frame

    # Update labels
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
