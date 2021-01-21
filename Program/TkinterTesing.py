from tkinter import *
from Node import Node
from Graph import Graph

class UserInterface:
    def __init__(self, master):
        lbl1 = Label(root, text="Enter graph size:")
        lbl2 = Label(root, text="Enter the start x value:")
        lbl3 = Label(root, text="Enter the start y value:")
        lbl4 = Label(root, text="Enter the end x value:")
        lbl5 = Label(root, text="Enter the end y value:")

        lbl1.grid(row=1, sticky=E)
        lbl2.grid(row=2, sticky=E)
        lbl3.grid(row=3, sticky=E)
        lbl4.grid(row=4, sticky=E)
        lbl5.grid(row=5, sticky=E)

        self.entry1 = Entry(root)
        self.entry2 = Entry(root)
        self.entry3 = Entry(root)
        self.entry4 = Entry(root)
        self.entry5 = Entry(root)

        self.entry1.grid(row=1, column=5)
        self.entry2.grid(row=2, column=5)
        self.entry3.grid(row=3, column=5)
        self.entry4.grid(row=4, column=5)
        self.entry5.grid(row=5, column=5)

        printButton = Button(root, text="Print")
        printButton.bind("<Button-1>", self.printSize)
        printButton.grid(row=6,column=10)

        displayBtn = Button(root, text="Display the graph")
        displayBtn.bind("<Button-1>", self.display)
        displayBtn.grid(row=7,column=10)

        startBtn = Button(root, text="Find Path")
        startBtn.bind("<Button-1>", self.findShortestPath)
        startBtn.grid(row=8, column=10)

    def printSize(self, event):
        print("Testing: " + self.entry1.get())

    def display(self, event):
        size = int(self.entry1.get())
        startX = int(self.entry2.get())
        startY = int(self.entry3.get())
        endX = int(self.entry4.get())
        endY = int(self.entry5.get())

        graph = Graph(size,startX,startY,endX,endY)
        graph.displayGraph()
        graph.findShortestPath()
        return

    def findShortestPath(self, event):
        graph.findShortestPath()

    def CloseWindow(self):
        root.quit()




root = Tk()
c = UserInterface(root)
root.geometry('1000x1000')
root.title('Tkinter Testing')
root.mainloop()


"""
---------------------------------------


import tkinter as tk

#window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text="Row")
        label.pack()

window.mainloop()




from tkinter import *

running = True  # Global flag

def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        print "hello"

    # After 1 second, call scanning again (create a recursive loop)
    root.after(1000, scanning)

def start():
    #Enable scanning by setting the global flag to True.
    global running
    running = True

def stop():
    #Stop scanning by setting the global flag to False
    global running
    running = False

root = Tk()
root.title("Thread testing")
root.geometry("500x500")

app = Frame(root)
app.grid()

start = Button(app, text="Start Scan", command=start)
stop = Button(app, text="Stop", command=stop)

start.grid()
stop.grid()

root.after(1000, scanning)  # After 1 second, call scanning
root.mainloop()
"""