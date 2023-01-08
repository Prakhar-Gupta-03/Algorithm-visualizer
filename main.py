from tkinter import *
from tkinter import ttk
import random


algorithm = ""
speed = ""
random_array = []
algorithms = ["Binary Search", "Kadane's Algorithm", "Selection Sort"]
speeds = ["Slow", "Medium", "Fast"]

def choose_algorithm():
    #sets the selected algorithm
    global algorithm
    algorithm = selected_algorithm.get()
    print(algorithm)

def choose_speed():
    #sets the selected speed
    global speed
    speed = selected_speed.get()
    print(speed)

def generate_array():
    #generates a random array of numbers 
    global random_array
    random_array = [random.randint(0,99) for i in range(15)]
    random_array.sort()
    for i in range(len(random_array)):
        label = Label(window, text = random_array[i], font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2)
        label.place(x = 150 + (i * 30), y = 230)

def reset():
    #reset the drop down menus
    global random_array, algorithm, speed
    selected_algorithm.set(algorithms[0])
    selected_speed.set(speeds[0])
    random_array = []
    algorithm = ""
    speed = ""

window = Tk()
window.geometry("800x600")
window.title("Algorithm Visualizer")

label_name = Label(window, text = "Algorithm Visualizer", font = ("Times New Roman", 20, "bold")).place(x = 275, y = 10)
label_choose_algorithm = Label(window, text = "Choose Algorithm: ", font = ("Times New Roman", 15, "bold")).place(x = 150, y = 100)
label_speed = Label(window, text = "Visualizer Speed: ", font = ("Times New Roman", 15, "bold")).place(x = 150, y = 140)

selected_algorithm = StringVar()
selected_speed = StringVar()
selected_algorithm.set(algorithms[0])
selected_speed.set(speeds[0])

dropDown_algorithms = OptionMenu(window, selected_algorithm, *algorithms)
dropDown_algorithms.config(width = 20, font = ("Times New Roman", 10), bg = "white", fg = "black")
dropDown_algorithms.place(x = 320, y = 100)
dropDown_speed = OptionMenu(window, selected_speed, *speeds)
dropDown_speed.config(width = 20, font = ("Times New Roman", 10), bg = "white", fg = "black")
dropDown_speed.place(x = 320, y = 140)
# button_run_algorithm = Button()
button_generate_array = Button(window, text="Generate Array", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: generate_array()).place(x = 270, y = 185)
button_reset = Button(window, text = "Reset", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: reset()).place(x = 400, y = 185)
button_run_algorithm = Button(window, text = "Run", font = ("Times New Roman", 10), bg = "white", fg = "black").place(x = 470, y = 185)
# button_choose_algorithm = Button(window, text = "Select Algorithm", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: choose_algorithm())
# button_choose_algorithm.place(x = 347, y = 150)


window.mainloop()

# frame = Frame(window, width=500, height=500, bg="white")
# frame.grid(row=0, column=0, padx=10, pady=10)
