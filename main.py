from tkinter import *
from tkinter import ttk
import random
import os
import time

#window definition
window = Tk()
window.geometry("800x600")
window.title("Algorithm Visualizer")

#constants and variables used everywhere in the code
label_current_element = Label()
label_left_element = Label()
label_right_element = Label()
label_mid_element = Label()
label_slow_pointer = Label()
label_fast_pointer = Label()
algorithm = ""
speed = ""
pace = 0
element_to_find = ""
label_search_element = Label(window, text = "Search Element: ", font = ("Times New Roman", 15, "bold"))
entry_search_element = Entry(window, font = ("Times New Roman", 10), bg = "white", fg = "black")
random_array = []
random_linked_list = []
random_array_elements = []
random_linked_list_elements = []
random_linked_list_arrows = []
algorithms = ["Linear Search","Binary Search", "Kadane's Algorithm", "Selection Sort", "Middle of Linked List", "Merge Sort"]
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
    global random_array, random_array_elements
    random_array = [random.randint(0,99) for i in range(15)]
    random_array.sort()
    random_array_elements = []
    for i in range(len(random_array)):
        label = Label(window, text = random_array[i], font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2, relief = "solid", borderwidth = 1)
        label.place(x = 150 + (i * 30), y = 270)
        random_array_elements.append(label)

# generates a random linked list of numbers of size 10
def generate_LL():
    global random_linked_list, random_linked_list_elements, random_linked_list_arrows
    random_linked_list = [random.randint(0,99) for i in range(11)]
    random_linked_list_elements = []
    for i in range(len(random_linked_list)):
        label = Label(window, text = random_linked_list[i], font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2, relief = "solid", borderwidth = 1)
        label1 = Label(window, text = "-->", font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2)	
        label.place(x = 150 + (i * 50), y = 270)
        label1.place(x = 150 + (i * 50) + 25, y = 270)
        random_linked_list_elements.append(label)
        random_linked_list_arrows.append(label1)

#displays the search element if the user selects linear search or binary search
def search_algo_element():
    label_search_element.place(x = 150, y = 230)
    entry_search_element.place(x = 320, y = 235)
    button_generate_array.place(x = 270, y = 185)

#displays the linked list generation button if the user selects the relevant algorithms only
def LL_algo_element():
    button_generate_LL.place(x = 270, y = 185)


#runs the linear search algorithm visualization
def linear_search():
    #runs the linear search algorithm
    global element_to_find, random_array, random_array_elements,label_current_element, speed, pace
    # setting the speed for the visualisation
    speed = selected_speed.get()
    if (speed=="Fast"): 
        pace = 0.2
    elif (speed=="Medium"):
        pace = 0.6
    else:
        pace = 1
    element_to_find = entry_search_element.get()
    element_to_find = int(element_to_find)
    found = False
    #traverse through the array and search for the element, and simultaneously show a label below the element which is being searched
    for i in range(len(random_array)):
        label_current_element = random_array_elements[i]
        if (random_array[i] == element_to_find):
            # label1 = Label(window, text = "|", font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2)
            # label1.place(x = 150 + (i * 30), y = 320)
            # label.config(bg = "blue")
            label_current_element.config(bg = "yellow")
            window.update()
            time.sleep(pace*3)
            label_current_element.config(bg = "white")
            window.update()
            found = True
            label_element_found = Label(window, text = "Element " + str(element_to_find) + " found", font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 20, height = 2)
            label_element_found.place(x = 150, y = 320)
            window.update()
            window.after(2000, label_element_found.destroy)
            break
        else:
            # label1 = Label(window, text = "|", font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 3, height = 2)
            # label1.place(x = 150 + (i * 30), y = 320)
            # label.config(bg = "red")
            #remove the label after 1 second
            label_current_element.config(bg = "red")
            window.update()
            time.sleep(pace)
            label_current_element.config(bg = "white")
            # window.after(1000, label1.destroy)
            window.update()
            # label.config(bg = "white")
    if (found == False):
        label_element_not_found = Label(window, text = "Element " + str(element_to_find) + " not found", font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 20, height = 2)
        label_element_not_found.place(x = 150, y = 320)
        window.update()
        window.after(2000, label_element_not_found.destroy)

#runs the binary search algorithm visualization
def binary_search():
    global element_to_find, random_array, random_array_elements, label_left_element, label_right_element, label_mid_element, speed, pace
    speed = selected_speed.get()
    if (speed=="Fast"): 
        pace = 0.2
    elif (speed=="Medium"):
        pace = 0.6
    else:
        pace = 1
    element_to_find = entry_search_element.get()
    element_to_find = int(element_to_find)
    left = 0
    right = len(random_array) - 1
    mid = left + (right - left)//2
    label_left_element = random_array_elements[left]
    label_right_element = random_array_elements[right]
    label_mid_element = random_array_elements[mid]
    label_left_element.config(bg = "yellow")
    label_right_element.config(bg = "yellow")
    label_mid_element.config(bg = "yellow")
    found = False
    window.update()
    while (left<=right):
        mid = left + (right - left)//2
        label_left_element = random_array_elements[left]
        label_right_element = random_array_elements[right]
        label_mid_element = random_array_elements[mid]
        label_left_element.config(bg = "yellow")
        label_right_element.config(bg = "yellow")
        label_mid_element.config(bg = "yellow")
        time.sleep(pace)
        window.update()
        if (element_to_find>random_array[mid]):
            label_left_element.config(bg = "white")
            label_mid_element.config(bg = "white")
            time.sleep(pace)
            window.update()
            left = mid + 1
        elif (element_to_find<random_array[mid]):
            label_right_element.config(bg = "white")
            label_mid_element.config(bg = "white")
            time.sleep(pace)
            window.update()
            right = mid-1
        else:
            found = True
            label_left_element.config(bg = "white")
            label_right_element.config(bg = "white")
            label_mid_element.config(bg = "red")
            window.update()
            time.sleep(pace*3)
            label_mid_element.config(bg = "white")
            window.update()
            break
    if (found):
        label_found = Label(window, text = "Element " + str(element_to_find) + " found at index " + str(mid), font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 20, height = 2)
        label_found.place(x = 150, y = 320)
        window.update()
        window.after(2000, label_found.destroy)
    else:
        label_not_found = Label(window, text = "Element " + str(element_to_find) + " not found", font = ("Times New Roman", 10, "bold"), bg = "white", fg = "black", width = 20, height = 2)
        label_not_found.place(x = 150, y = 320)
        window.update()
        window.after(2000, label_not_found.destroy)

#runs the algorithm to find the middle of the linked list
def middle_LL():
    global random_linked_list, random_linked_list_elements, label_slow_pointer, label_fast_pointer, pace, speed
    speed = selected_speed.get()
    if (speed=="Fast"): 
        pace = 0.2
    elif (speed=="Medium"):
        pace = 0.6
    else:
        pace = 1
    #find the middle of the linked list
    slow = 0
    fast = 0
    N = len(random_linked_list) - 1
    label_fast_pointer = random_linked_list_elements[fast]
    label_slow_pointer = random_linked_list_elements[slow]
    label_fast_pointer.config(bg = "yellow")
    label_slow_pointer.config(bg = "yellow")
    window.update()
    while (fast<N and fast+1<N):
        label_fast_pointer.config(bg = "white")
        label_slow_pointer.config(bg = "white")
        time.sleep(pace)
        window.update()
        slow = slow + 1
        fast = fast + 2
        label_fast_pointer = random_linked_list_elements[fast]
        label_slow_pointer = random_linked_list_elements[slow]
        label_fast_pointer.config(bg = "yellow")
        label_slow_pointer.config(bg = "yellow")
        window.update()
        time.sleep(pace)
    if (fast == N):
        label_fast_pointer.config(bg = "white")
        label_slow_pointer.config(bg = "red")
        window.update()
        time.sleep(2.5)
        label_slow_pointer.config(bg = "white")
        window.update()
    else:
        label_fast_pointer.config(bg = "white")
        label_slow_pointer.config(bg = "white")
        label_slow_pointer = random_linked_list_elements[slow+1]
        label_slow_pointer.config(bg = "red")
        window.update()
        time.sleep(2.5)
        label_slow_pointer.config(bg = "white")
        window.update()

#runs the selected algorithm
def run_algorithm():
    global algorithm
    algorithm = selected_algorithm.get()
    if (algorithm == "Linear Search"):
        linear_search()
    elif (algorithm == "Binary Search"):
        binary_search()
    elif (algorithm == "Middle of Linked List"):
        middle_LL()

#resets all default values
def reset():
    #reset the drop down menus
    global label, random_array, algorithm, speed, random_array_elements, random_linked_list, label_left_element, label_right_element, label_mid_element, random_linked_list_elements, random_linked_list_arrows
    selected_algorithm.set(algorithms[0])
    selected_speed.set(speeds[0])
    algorithm = "" 
    speed = ""
    #remove the array elements from the screen
    for i in range(0, len(random_array_elements)):
        label = random_array_elements[i]
        #delete label from screen
        window.after(0, label.destroy)
    #remove the linked list elements from the screen
    for i in range(0, len(random_linked_list_elements)):
        label = random_linked_list_elements[i]
        #delete label from screen
        window.after(0, label.destroy)
        # label.destroy()
    #reset the linked list elements
    for i in range(0, len(random_linked_list)):
        label = random_linked_list_elements[i]
        window.after(0, label.destroy)
    for i in range(0, len(random_linked_list)):
        label = random_linked_list_arrows[i]
        window.after(0, label.destroy)
    random_array = []
    random_linked_list = []
    random_linked_list_elements = []
    random_linked_list_arrows = []
    random_array_elements = []
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
button_generate_array = Button(window, text="Generate Array", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: generate_array())
button_generate_LL = Button(window, text = "Generate Linked List", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: generate_LL())
button_reset = Button(window, text = "Reset", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: reset()).place(x = 400, y = 185)
button_run_algorithm = Button(window, text = "Run", font = ("Times New Roman", 10), bg = "white", fg = "black", command = lambda: run_algorithm()).place(x = 470, y = 185)

#if the user selects linear search or binary search, then the search element will be displayed
selected_algorithm.trace("w", lambda *args: search_algo_element() if (selected_algorithm.get() == "Linear Search" or selected_algorithm.get() == "Binary Search") else label_search_element.place_forget())
selected_algorithm.trace("w", lambda *args: search_algo_element() if (selected_algorithm.get() == "Linear Search" or selected_algorithm.get() == "Binary Search") else entry_search_element.place_forget())
selected_algorithm.trace("w", lambda *args: search_algo_element() if (selected_algorithm.get() == "Linear Search" or selected_algorithm.get() == "Binary Search" or selected_algorithm.get() == "Selection Sort" or selected_algorithm.get() == "Kadane's Algorithm" or selected_algorithm.get() == "Merge Sort") else button_generate_array.place_forget())
selected_algorithm.trace("w", lambda *args: LL_algo_element() if (selected_algorithm.get() == "Middle of Linked List") else button_generate_LL.place_forget())

#renders the window continuously
window.mainloop()

# frame = Frame(window, width=500, height=500, bg="white")
# frame.grid(row=0, column=0, padx=10, pady=10)

