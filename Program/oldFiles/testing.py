from tkinter import *

class UserInterface:
    def __init__(self, master):
        lbl1 = Label(root, text="Enter graph size:")
        lbl1.grid(row=1, sticky=E)

        self.entry1 = Entry(root)
        self.entry1.grid(row=1, column=5)
        
        printButton = Button(root, text="Print")
        printButton.bind("<Button-1>", self.printSize)
        printButton.grid(row=2,column=10)

      
    def printSize(self, event):
        print("Testing: " + self.entry1.get())

root = Tk()
c = UserInterface(root)
root.geometry('500x500')
root.title('Tkinter Testing')
root.mainloop()