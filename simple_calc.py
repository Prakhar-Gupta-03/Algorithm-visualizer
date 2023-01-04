from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Simple Calculator")
window.configure(background = "grey")

entry = Entry(window, width = 50)
# entry.pack()

def zero_click():
    entry.insert(END, "0")
def one_click():
    entry.insert(END, "1")
def two_click():
    entry.insert(END, "2")
def three_click():
    entry.insert(END, "3")
def four_click():
    entry.insert(END, "4")
def five_click():
    entry.insert(END, "5")
def six_click():
    entry.insert(END, "6")
def seven_click():
    entry.insert(END, "7")
def eight_click():
    entry.insert(END, "8")
def nine_click():
    entry.insert(END, "9")
def plus_click():
    entry.insert(END, "+")
def minus_click():
    entry.insert(END, "-")
def multiply_click():
    entry.insert(END, "*")
def divide_click():
    entry.insert(END, "/")
def clear_click():
    entry.delete(0, END)
def calculate_click():
    query = entry.get()
    result = eval(query)
    entry.delete(0, END)
    entry.insert(0, result)

zero = Button(window, text = "0", command = zero_click)
one = Button(window, text = "1", command = one_click)
two = Button(window, text = "2", command = two_click)
three = Button(window, text = "3", command = three_click)
four = Button(window, text = "4", command = four_click)
five = Button(window, text = "5", command = five_click)
six = Button(window, text = "6", command = six_click)
seven = Button(window, text = "7", command = seven_click)
eight = Button(window, text = "8", command = eight_click)
nine = Button(window, text = "9", command = nine_click)
plus = Button(window, text = "+", command = plus_click)
minus = Button(window, text = "-", command = minus_click)
multiply = Button(window, text = "*", command = multiply_click)
divide = Button(window, text = "/", command = divide_click)
equal = Button(window, text = "=", command = calculate_click)
clear = Button(window, text = "Clear", command = clear_click)
zero.grid(row = 0, column = 0)
one.grid(row = 0, column = 1)
two.grid(row = 0, column = 2)
three.grid(row = 1, column = 0)
four.grid(row = 1, column = 1)
five.grid(row = 1, column = 2)
six.grid(row = 2, column = 0)
seven.grid(row = 2, column = 1)
eight.grid(row = 2, column = 2)
nine.grid(row = 3, column = 0)
plus.grid(row = 3, column = 1)
minus.grid(row = 3, column = 2)
multiply.grid(row = 4, column = 0)
divide.grid(row = 4, column = 1)
equal.grid(row = 4, column = 2)
clear.grid(row = 5, column = 0)
entry.grid(row = 5, column = 1, columnspan = 2)
window.mainloop()