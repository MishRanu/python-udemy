#tkinter module and python provides access tk toolkit, made to work with a programming language called tcl
#tkinter is a part of the standard python language
#the documentation of tkinter isn't brilliant, and there has been improvement with newer versions of tkinter
#themed widgets in 2015 is good, and you can provide some good nice interfaces with it

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# mainWindow = tkinter.Tk()
# mainWindow.title("Hello World")
# mainWindow.geometry("840x640")
# mainWindow.mainloop()
# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello World!")
mainWindow.geometry("640x480")

#Window can be placed at places using window managers
#not ever window
#we are going to start with pack manager
#every window must have a master window
#we will use canvas window
#stract a widget horizontally and vertically

label = tkinter.Label(mainWindow, text = "Hello World")
label.pack(side = "top")

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)


canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.pack(side="left")

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side = "right", anchor = "n", expand=True)

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")

mainWindow.mainloop()

#Of the 3 geometry mamagers that come with tkinter pack is the most basis of them