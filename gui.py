#Lark Inostroza
#Simple GUI using PySimpleGUI to create a bar plot comparing the time between each algo and accepts an arbitrary number from the user to define list length.
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Layout
layout = [
    [sg.Text("Enter the length of the list: "), sg.InputText(key='length')],
    [sg.Button('Analyze')],
    [sg.Canvas(key='plot_canvas', size=(400, 400))],
]

#Create window
window = sg.Window('Algorithm Comparison', layout)

#Where you put your data
def analyze_algorithms(length):
    algorithms = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3']#Placeholder
    execution_times = [10, 15, 20]#Placeholder
    return algorithms, execution_times

#Generate bar plot
def generate_bar_plot(algorithms, execution_times):
    plt.figure()
    plt.bar(algorithms, execution_times)
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
        length = int(values['length'])
        
        algorithms, execution_times = analyze_algorithms(length)
        
        #Generate/update bar plot
        if 'fig_agg' in globals():
            window['plot_canvas'].TKCanvas.delete_figure(fig_agg)
        fig_agg = generate_bar_plot(algorithms, execution_times)

window.close()