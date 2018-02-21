#in the last lecture we discuseed pack geometry manager
#in this video we will be discussing about the place geometry manager

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World!")
mainWindow.geometry("640x480+8+200")

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side="left", fill=tkinter.Y, anchor="n", expand=False)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)
# canvas.pack(side="left", anchor="n")

rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side="right", anchor = "n", expand=True)
rightFrame.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

button1.grid(row=0, column=0)
# button1.pack(side="top")
# button2.pack(side="top")
button2.grid(row=1, column=0)

# button3.pack(side="top")
button3.grid(row=2, column=0)

#configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

leftFrame.config(relief="sunken", borderwidth=1)
rightFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")

mainWindow.mainloop()
a
#package is one of the most basic pakcages associated