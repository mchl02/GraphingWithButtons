import matplotlib
matplotlib.use('TkAgg')


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
from math import *



root = Tk.Tk()
root.wm_title("Embedding in TK")

f = Figure(figsize=(5,3), dpi=100)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas.show()

#Graph a scatterplot 
def first():
    x_list_for_y_2 = []
    y_list_for_y_2 = []
    #Takes one third of the available space
    a = f.add_subplot(131)
    for ranger in xrange(10):
        x_list_for_y_2.append(ranger)
        y = ranger + 2
        y_list_for_y_2.append(y)
    a.scatter(x_list_for_y_2,y_list_for_y_2)

#    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
#    canvas.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

#    toolbar = NavigationToolbar2TkAgg( canvas, root )
#    toolbar.update()
#    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def second():
    X_Axis = []
    Y_Axis = []
#    f = Figure(figsize=(5,3), dpi=100)
    #Takes one third of the available space
    a = f.add_subplot(132)
    for hi in xrange(10):
        X_Axis.append(hi)
        Y_Axis.append(hi)
    a.plot(X_Axis, Y_Axis)
#    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
#    canvas.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

#    toolbar = NavigationToolbar2TkAgg( canvas, root )
#    toolbar.update()
#    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def third():
    Matt = []
    Lee = []
#    f = Figure(figsize=(5,3), dpi = 100)
    #Takes one third of the available space
    a = f.add_subplot(133)
    for numbers in xrange(10):
        Matt.append(numbers - (numbers * 2))
        answer = (numbers - (numbers * 2)) - 4
        Lee.append(answer)
    a.plot(Matt,Lee)
#    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
#    canvas.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

#    toolbar = NavigationToolbar2TkAgg( canvas, root )
#    toolbar.update()
#    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


#Tkinter below
button1 = Tk.Button(text = "Press Me To Graph y = x + 2", command = first)
button1.pack()
button2 = Tk.Button(text = "Press Me to Graph y = x", command = second)
button2.pack()
button3 = Tk.Button(text = "Press Me to Graph y = -x - 4", command = third)
button3.pack()
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
                                   
Tk.mainloop()