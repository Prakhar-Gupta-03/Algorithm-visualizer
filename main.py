from tkinter import *
from tkinter import ttk
import random
import os
import time

#window definition
window = Tk()
window.geometry("800x600")
window.title("Algorithm Visualizer")

label_current_element = Label()
algorithm = ""
speed = ""
element_to_find = ""
label_search_element = Label(window, text = "Search Element: ", font = ("Times New Roman", 15, "bold"))
entry_search_element = Entry(window, font = ("Times New Roman", 10), bg = "white", fg = "black")
random_array = []
random_array_elements = []
algorithms = ["Linear Search","Binary Search", "Kadane's Algorithm", "Selection Sort"]
speeds = ["Slow", "Medium", "Fast"]
linear_search_iterator = Label(window, text = "hello", font = ("Times New Roman", 10, "bold"), width = 10, height = 10)

#functions
#chooses the algorithm from the drop down menu
def choose_algorithm():
    #sets the selected algorithm
    global algorithm
    algorithm = selected_algorithm.get()
    print(algorithm)
#chooses the speed from the drop down menu
def choose_speed():
    #sets the selected speed
    global speed
    speed = selected_speed.get()
    print(speed)

#generates a random array of numbers of size 15
def generate_array():
    #generates a random array of numbers 
    global random_array
    random_array = [random.randint(0,99) for i in range(15)]
    random_array.sort()
    for i in range(len(random_array)):
        label = Label(window, text = random_array[i], font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2)
        label.place(x = 150 + (i * 30), y = 270)
        # window.update()
        # time.sleep(1)
        # label.config(bg = "green")
        random_array_elements.append(label)
        # window.update()

#displays the search element if the user selects linear search or binary search
def search_algo_element():
    label_search_element.place(x = 150, y = 230)
    entry_search_element.place(x = 320, y = 235)

#runs the linear search algorithm visualization
def linear_search():
    #runs the linear search algorithm
    global element_to_find, random_array, random_array_elements,label_current_element
    element_to_find = entry_search_element.get()
    element_to_find = int(element_to_find)
    #traverse through the array and search for the element, and simultaneously show a label below the element which is being searched
    for i in range(len(random_array)):
        label_current_element = random_array_elements[i]
        if (random_array[i] == element_to_find):
            # label1 = Label(window, text = "|", font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2)
            # label1.place(x = 150 + (i * 30), y = 320)
            # label.config(bg = "blue")
            label_current_element.config(bg = "yellow")
            window.update()
            time.sleep(2)
            label_current_element.config(bg = "white")
            window.update()
            break
        else:
            # label1 = Label(window, text = "|", font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2)
            # label1.place(x = 150 + (i * 30), y = 320)
            # label.config(bg = "red")
            #remove the label after 1 second
            print("current element:", random_array[i])
            label_current_element.config(bg = "red")
            window.update()
            time.sleep(1)
            label_current_element.config(bg = "white")
            # window.after(1000, label1.destroy)
            window.update()
            # label.config(bg = "white")

#runs the binary search algorithm visualization
def run_algorithm():
    global algorithm
    algorithm = selected_algorithm.get()
    if (algorithm == "Linear Search"):
        linear_search()

#resets the drop down menus
def reset():
    #reset the drop down menus
    global random_array, algorithm, speed
    selected_algorithm.set(algorithms[0])
    selected_speed.set(speeds[0])
    random_array = []
    algorithm = ""
    speed = ""

#window elements
label_name = Label(window, text = "Algorithm Visualizer", font = ("Times New Roman", 20, "bold")).place(x = 275, y = 10)
label_choose_algorithm = Label(window, text = "Choose Algorithm: ", font = ("Times New Roman", 15, "bold")).place(x = 150, y = 100)
label_speed = Label(window, text = "Visualizer Speed: ", font = ("Times New Roman", 15, "bold")).place(x = 150, y = 140)

#defalut values for drop down menus
selected_algorithm = StringVar()
selected_speed = StringVar()
selected_algorithm.set(algorithms[0])
selected_speed.set(speeds[0])

#drop down menus
dropDown_algorithms = OptionMenu(window, selected_algorithm, *algorithms)
dropDown_algorithms.config(width = 20, font = ("Times New Roman", 10), bg = "white", fg = "black")
dropDown_algorithms.place(x = 320, y = 100)
dropDown_speed = OptionMenu(window, selected_speed, *speeds)
dropDown_speed.config(width = 20, font = ("Times New Roman", 10), bg = "white", fg = "black")
dropDown_speed.place(x = 320, y = 140)

#buttons
button_generate_array = Button(window, text="Generate Array", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: generate_array()).place(x = 270, y = 185)
button_reset = Button(window, text = "Reset", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: reset()).place(x = 400, y = 185)
button_run_algorithm = Button(window, text = "Run", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: run_algorithm()).place(x = 470, y = 185)

#if the user selects linear search or binary search, then the search element will be displayed
selected_algorithm.trace("w", lambda *args: search_algo_element() if (selected_algorithm.get() == "Linear Search" or selected_algorithm.get() == "Binary Search") else label_search_element.place_forget())
selected_algorithm.trace("w", lambda *args: search_algo_element() if (selected_algorithm.get() == "Linear Search" or selected_algorithm.get() == "Binary Search") else entry_search_element.place_forget())
#renders the window continuously
window.mainloop()

# frame = Frame(window, width=500, height=500, bg="white")
# frame.grid(row=0, column=0, padx=10, pady=10)

