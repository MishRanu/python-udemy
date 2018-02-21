# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import math
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("300x300-8-200")
mainWindow["padx"]=8



#I can create a string var that parses the expression entered through the entry
#but currently I am just interested in making the layout rather than the underlaying functionality
#so I will continue to code1

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky="ew", columnspan=5)


mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)

# calcPanel=tkinter.Frame(mainWindow)
# calcPanel.grid(row=1, column=0, rowspan=6, columnspan=5, sticky="nsew")

calcLayout = [("C", 1), ("CE", 1), ("", 1), ("", 1), ("7",1), ("8",1), ("9",1), ("+",1), ("4",1), ("5",1), ("6",1), ("-",1), ("1",1), ("2",1), ("3",1), ("*",1), ("0",1), ("=",2), ("/",1)]
inputButtons = []
i=0
r=1
c=0
print(len(calcLayout))

while i < len(calcLayout):
    r = math.floor((i)/4)+1
    c=c%4
    if(calcLayout[i][0]!=""):
        inputButtons.append(tkinter.Button(mainWindow, text=calcLayout[i][0]))
        inputButtons[len(inputButtons)-1].grid(row=r, column=c, columnspan=calcLayout[i][1], sticky="nsew")
    c+=calcLayout[i][1]
    i+=1



mainWindow.mainloop()