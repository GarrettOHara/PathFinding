from Node import Node
from Graph import Graph
from tkinter import * 
from tkinter.ttk import *


master = Tk()
class Driver:
    size = int(input("Enter the size of the graph: "))
    startX = int(input("Enter the x value of the start node: "))
    startY = int(input("Enter the y value of the start node: "))
    endX = int(input("Enter the x value of the end node: "))
    endY = int(input("Enter the y value of the end node: "))
    NODE_WIDTH = 50
    
    label1 = Label(master, text = "Enter the size of the graph:")
    label2 = Label(master, text = "Enter start x:")
    label3 = Label(master, text = "Enter start y:")
    label4 = Label(master, text = "Enter end x:")
    label5 = Label(master, text = "Enter end y:")

    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)

    e1.grid(row = 0, column = 1, pady = 2)
    e2.grid(row = 1, column = 1, pady = 2)
    e3.grid(row = 2, column = 1, pady = 2)
    e4.grid(row = 3, column = 1, pady = 2)
    e5.grid(row = 4, column = 1, pady = 2)

    mainloop()

    graph = Graph(size,startX,startY,endX,endY)
    graph.displayGraph()
    print("")
    graph.findShortestPath()