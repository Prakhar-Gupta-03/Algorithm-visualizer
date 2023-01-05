from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Algorithm Visualizer")
window.configure(background = "grey")
def choose_algorithm():
    print(selected_algorithm.get())
#define a list of algorithms
algorithms = ["Binary Search", "Kadane's Algorithm", "Selection Sort"]
# holds the seleted algorithm
selected_algorithm = StringVar()
# set the default value
selected_algorithm.set(algorithms[0])
drop_down = OptionMenu(window, selected_algorithm, *algorithms)
#defining a label
choose_algorithm_label = Label(window, text = "Choose Algorithm:").grid(row = 0, column = 0, padx = 10, pady = 10)
drop_down.grid(row = 0, column = 1, padx = 10, pady = 10)
choose_algorithm = Button(window, text = "Choose Algorithm", command = choose_algorithm)
choose_algorithm.grid(row = 1, column = 0, padx = 10, pady = 10)
window.mainloop()