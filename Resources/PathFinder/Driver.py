import tkinter as tk
from GUI import Graph

def main():
    dimensions = [10,10]
    start = [1,1]
    end = [9,9]
    message =\
    """
------------------------------------------------\n
        Welcome to A* Path Finder\n
-------------------------------------------------\n
A* Path Finder allows you to customize your own
graph with two starting points, and create
obsticles the algorithm will find the shortest
path possible between your maze!\n
Would you like to customize your graph? [y/n]: """

    errorMessage =\
    """
    
Invalid input, please try again
Please type \'y\' for yes or \'n\' no
Would you like to customize your graph? [y/n]: """

    #startNode = Node()

    user = input(message)
    while (user != 'y' and user != 'n'):
        user = input(errorMessage)
    if user == 'y':
        dimensions = []
        start = []
        end = []
        print()
        dimensions.append(int(input("How many rows should the graph have?        ")))
        dimensions.append(int(input("How many columns should the graph have?     ")))
        start.append(int(input("What is the x value of the starting point?  ")))
        start.append(int(input("What is the y value of the starting point?  ")))
        end.append(int(input("What is the x value of the starting point?  ")))
        end.append(int(input("What is the y value of the starting point?  ")))

        print("Graph Dimensions: ", dimensions)
        print("Starting point:   ", start)
        print("Ending point:     ", end)

    
    window = tk.Tk()
    w = Graph(window, dimensions[0], dimensions[1])#, start[0], start[1], end[0], end[1])#start, end)
    w.pack(expand=True, fill=tk.BOTH)
    window.title('Path Finder')
    window.mainloop()

if __name__ == '__main__':
    main()