from tkinter import *
from random import randint
 
# these two imports are important
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading
 
continuePlotting = False
e = "none"

def printtext():
    global e
    string = e.get() 
    print (string)
 
def change_state():
    global continuePlotting
    if continuePlotting == True:
        continuePlotting = False
    else:
        continuePlotting = True
    
 
def data_points():
    f = open("data.txt", "w")
    for i in range(10):
        f.write(str(randint(0, 10))+'\n')
    f.close()
 
    f = open("data.txt", "r")
    data = f.readlines()
    f.close()
 
    l = []
    for i in range(len(data)):
        l.append(int(data[i].rstrip("\n")))
    return l
 
def app():
    # initialise a window.
    root = Tk()
    root.config(background='white')
    root.geometry("1000x700")

    root.title('Testing...')

    
    e = Entry(root)
    e.pack()

    e.focus_set()

    def callback():
        print (e.get())

    b = Button(root, text="get", width=10, command=callback)
    b.pack()
    
    lab = Label(root, text="Live Plotting", bg = 'white').pack()
    
    fig = Figure(figsize=(10,4))
    #fig.set_dpi(150)
    #fig.set_size_inches(5, 5, forward=True)

    ax = fig.add_subplot(121)
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature")
    ax.grid()   

    ax2 = fig.add_subplot(122)
    ax2.set_xlabel("Intensity")
    ax2.set_ylabel("Wave Length")
    ax2.grid()
 
    graph = FigureCanvasTkAgg(fig, master=root)
    graph.get_tk_widget().pack(side="top",fill='none',expand=False)
 
    def plotter():
        while continuePlotting:
            ax.cla()
            ax.grid()
            dpts = data_points()
            ax.plot(range(10), dpts, marker='o', color='orange')
            graph.draw()
            time.sleep(1)
 
    def gui_handler():
        change_state()
        plotter()
        #threading.Thread(target=plotter).start()
 
    b = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    b.pack()
    
    root.mainloop()
 
if __name__ == '__main__':
    app()