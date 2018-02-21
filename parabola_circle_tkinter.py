try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import math

def calc_parabola_y(x):
    return x*x

def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width()/2
    y_origin = canvas.winfo_height()/2
    canvas.config(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))

    #creating the x axis
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    #creating the y axis
    canvas.create_line(0, -y_origin, 0, y_origin, fill="black")


def make_parabola(x):
    for i in range(-100*x, 100*x):
        yi=calc_parabola_y(i/100)
        canvas.create_line(i/100, -yi/100, (i+1)/100 ,(-yi-1)/100, fill="red")



#exempted from writing the complete code due to sleeping issues
def make_circle(r):
    r=100*r
    for x in range(0, r):
        x = x/100
        y=math.sqrt(math.pow(r/100,2)-math.pow(x,2))
        canvas.create_line(x,-y,x+1, -y-1, fill="blue")
        canvas.create_line(x,y,x+1, y+1, fill="blue")
        canvas.create_line(-x,-y,-x-1, -y-1, fill="blue")
        canvas.create_line(-x,y,-x-1, y+1, fill="blue")

mainWindow = tkinter.Tk()
mainWindow.title("Parabola construction")
mainWindow.geometry("400x400")


canvas = tkinter.Canvas(mainWindow)
canvas.grid(row=0, column=0, sticky="ew")

draw_axes(canvas)
make_parabola(100)
# n = input("enter the range for the parabola \n")
make_circle(50)
mainWindow.mainloop()