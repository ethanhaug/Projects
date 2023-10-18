"""
Calcul8r Alig8r: the awesomest calculator app in existence.
"""

import tkinter as tk
from tkinter import ttk


class Calculator:
    """ Model for a simple accumulating calculator with support for a limited set of arithmetic operations. """

    _accumulator: int

    def __init__(self) -> None:
        self._accumulator = 0

    def set_accumulator(self, num: int) -> None:
        """ Sets the accumulator to the given <num>. """
        self._accumulator = num

    def add(self, num: int) -> int:
        """ Adds <num> to the accumulator, returning the updated value for the accumulator. """
        self._accumulator += num
        return self._accumulator

    def subtract(self, num: int) -> int:

        self._accumulator -= num
        return self._accumulator


class CalculatorApp(tk.Tk):
    """ GUI class based on TKinter. """

    # important instance variables
    display: tk.Label
    calculator: Calculator
    last_op: str

    def __init__(self, calc: Calculator):
        """ Sets the title, creates the layout, then sets actions to run for events. """
        super().__init__()
        self.title("Calcul8r Alig8r")
        self.create_layout()
        self.set_commands()

        self.calculator = calc
        self.calculator.set_accumulator(0)

        self.last_op = None

    def set_commands(self):
        """ Sets the event handlers for the application. """
        def append0():
            self.display['text'] += '0'

        def append1():
            self.display['text'] += '1'

        def append2():
            self.display['text'] += '2'

        def append3():
            self.display['text'] += '3'

        def append4():
            self.display['text'] += '4'

        def append5():
            self.display['text'] += '5'

        def append6():
            self.display['text'] += '6'

        def append7():
            self.display['text'] += '7'

        def append8():
            self.display['text'] += '8'

        def append9():
            self.display['text'] += '9'

        def start_add():
            self.last_op = "+"
            self.calculator.add(int(self.display['text']))
            self.display['text'] = '0'

        def start_subract():
            self.last_op = "-"
            self.calculator.subtract(int(self.display['text']))
            self.display['text'] = '0'

        def perform_calculation():
            if self.last_op == '+':
                focus = int(self.display['text'])
                var = self.calculator.add(focus)
                self.display['text'] = str(var)
            elif self.last_op == '-':
                focus = int(self.display['text'])
                var = self.calculator.subtract(focus)
                self.display['text'] = str(var)

        self.zero_button['command'] = append0
        self.one_button['command'] = append1
        self.two_button['command'] = append2
        self.three_button['command'] = append3
        self.four_button['command'] = append4
        self.five_button['command'] = append5
        self.six_button['command'] = append6
        self.seven_button['command'] = append7
        self.eight_button['command'] = append8
        self.nine_button['command'] = append9
        self.plus_button['command'] = start_add
        self.minus_button['command'] = start_subract
        self.equal_button['command'] = perform_calculation

    def create_layout(self):
        """ Creates the widgets and lays them out in the application window. """

        # Create Frame to hold the number display and undo/clear buttons
        display_frame = tk.Frame(self)
        display_frame.grid(row=0, column=0, columnspan=5)

        # create number display (a Label) and clear/undo buttons and place them
        # within the display_frame using the grid layout manager

        self.display = tk.Label(display_frame, bg="white",
                                fg="black", text="0", width=15, height=2)
        self.undo_button = tk.Button(display_frame, text="Undo")
        self.clear_button = tk.Button(display_frame, text="Clear")

        self.display.grid(row=0, column=0, columnspan=4, rowspan=2)
        self.undo_button.grid(row=0, column=4)
        self.clear_button.grid(row=1, column=4)

        # Create Frame to hold the operator (e.g. +, -, ...) buttons
        operators_frame = tk.Frame(self)
        operators_frame.grid(row=1, column=0, columnspan=5)

        # create operator buttons and place them within the operators_frame using
        # the grid layout manager

        self.plus_button = tk.Button(operators_frame, text="+")
        self.minus_button = tk.Button(operators_frame, text="-")
        self.divide_button = tk.Button(operators_frame, text="/")
        self.multiply_button = tk.Button(operators_frame, text="x")
        self.power_button = tk.Button(operators_frame, text="^")

        self.plus_button.grid(row=1, column=1)
        self.minus_button.grid(row=1, column=2)
        self.divide_button.grid(row=1, column=3)
        self.multiply_button.grid(row=1, column=4)
        self.power_button.grid(row=1, column=5)

        # Create Frame to hold the number and = buttons
        numbers_frame = tk.Frame(self)
        numbers_frame.grid(row=2, column=0, columnspan=4)

        # create number and = buttons and place them within the numbers_frame using
        # the grid layout manager

        self.equal_button = tk.Button(numbers_frame, text="=")
        self.one_button = tk.Button(numbers_frame, text="1")
        self.two_button = tk.Button(numbers_frame, text="2")
        self.three_button = tk.Button(numbers_frame, text="3")
        self.four_button = tk.Button(numbers_frame, text="4")
        self.five_button = tk.Button(numbers_frame, text="5")
        self.six_button = tk.Button(numbers_frame, text="6")
        self.seven_button = tk.Button(numbers_frame, text="7")
        self.eight_button = tk.Button(numbers_frame, text="8")
        self.nine_button = tk.Button(numbers_frame, text="9")
        self.zero_button = tk.Button(numbers_frame, text="0")

        # top row of numbers
        self.seven_button.grid(row=0, column=0)
        self.eight_button.grid(row=0, column=1)
        self.nine_button.grid(row=0, column=2)

        # second row of numbers
        self.four_button.grid(row=1, column=0)
        self.five_button.grid(row=1, column=1)
        self.six_button.grid(row=1, column=2)

        # third row of numbers
        self.one_button.grid(row=2, column=0)
        self.two_button.grid(row=2, column=1)
        self.three_button.grid(row=2, column=2)

        # bottom row of numbers (and =)
        self.zero_button.grid(row=3, column=0, columnspan=2, sticky="we")
        self.equal_button.grid(row=3, column=2)

    def set_display(self, num: int) -> None:
        """ Updates the text shown in the display to <num>. """
        self.display['text'] = str(num)


calculator = Calculator()
app = CalculatorApp(calculator)
app.mainloop()  # Start the GUI event loop
