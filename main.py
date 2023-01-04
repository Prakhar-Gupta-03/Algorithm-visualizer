from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Algorithms Visualizer")
window.configure(background = "grey");
firstLabel = Label(window, text="First Label")
firstLabel.grid(row = 0, column = 0)
secondLabel = Label(window, text = "Second  Label")
secondLabel.grid(row = 1, column = 0)
window.mainloop()