#Lark Inostroza
#Simple GUI using PySimpleGUI to create a bar plot comparing the time between each algo and accepts an arbitrary number from the user to define list length.
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import timeit
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Algorithms
def bubble_sort(L): # O(1)
    n = len(L)
    for i in range(n): # n-1 times O(n)
        for j in range(0, n - 1 - 1): # N-i-1 times O(n)
            if L[j] > L[j+1]: # 0(n)
                L[j], L[j+1], L[j] # O(N^2)
    return L # O(1)

def merge_sort(arr):
    if len(arr) > 1: #check if the array has more than one element
        mid = len(arr) // 2 #find the midpoint of array
        L = arr[:mid] # create left sublist and assigning the first half 
        R = arr[mid:] # create right sublsit and assign the second half 

        merge_sort(L) # recursively applies Merge sort to the left sublist 
        merge_sort(R) # recursively applies Merge sort to the right sublist 
        i = j = k = 0 # i for the current index of the left sublsit 
                # j for the current index if the right sublsit 
                # k for the current index of main arr

        while i < len(L) and j < len(R): #continue the loop as long as there are...
            if L[i] < R[j]: # check if the current elemnt in the left sublist...
                arr[k] = L[i] # if true, place the current left elemtn into the...
                i += 1 #moves the pointer in the left sublsit 
            else:
                arr[k] = R[j] # place the current element from right sublist 
                j += 1 # moves pointer in teh right sublist
            k += 1 #regardless of whre the elemnt was taken from, pointer of main array must move on.

        while i < len(L): #handle the scenario where one sublsit is exhauseted before
            arr[k] = L[i] # copy the remaining element from L or R into the arr
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    # if the array is empty or has a single element, it's already sorted.
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the middle element as the pivot.
        pivot = arr[len(arr) // 2]
        left = []  # Elements less than the pivot.
        middle = []  # Elements equal to the pivot.
        right = []  # Elements greater than the pivot.

        # Partitioning the array based on the pivot value.
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)

        # Recursively sorting the left and right parts of the array, and concatenating the results.
        return quick_sort(left) + middle + quick_sort(right)

#Layout
layout = [
    [sg.Text("Enter the length of the list: "), sg.InputText(key='length')],
    [sg.Button('Analyze')],
    [sg.Canvas(key='plot_canvas', size=(400, 400))],
]

#Create window
window = sg.Window('Algorithm Comparison', layout)
def random_list(size):
    res = []
    for _ in range(0, size):
        res.append(random.randint(0, 100000)) # arbitrary range, subject to change
    return res

# Return name and runtime of algorithm
def analyze_algorithms(length):
    algorithms = {
        'Bubble Sort': timeit.timeit(lambda: bubble_sort(random_list(length)), number=1),
        'Merge Sort': timeit.timeit(lambda: merge_sort(random_list(length)), number=1),
        'Quick Sort': timeit.timeit(lambda: quick_sort(random_list(length)), number=1),
    }
    return algorithms.keys(), algorithms.values()

#Generate bar plot
def generate_bar_plot(algorithms, execution_times):
    plt.figure()
    bar = plt.bar(algorithms, execution_times)
    # truncate decimal points
    plt.bar_label(bar, labels=[round(time, 5) for time in execution_times])
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time')
    plt.title('Algorithm Comparison') 
    fig_canvas_agg = FigureCanvasTkAgg(plt.gcf(), window['plot_canvas'].TKCanvas)
    fig_canvas_agg.draw()
    fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return fig_canvas_agg

#loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Analyze':
        # Input handling
        # Invalid lengths are strings, floats, and numbers <= 0
        try:
            length = int(values['length'])
            if length <= 0:
                raise Exception
        except Exception: # invalid input:
            window['length'].update(value="Invalid input")
            continue
        
        algorithm_names, execution_times = analyze_algorithms(length)
        
        #Generate/update bar plot
        if 'fig_agg' in globals():
            fig_agg.get_tk_widget().pack_forget() 
        fig_agg = generate_bar_plot(algorithm_names, execution_times)

window.close()