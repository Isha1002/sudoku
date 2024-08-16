import tkinter as tk
from tkinter import *
from tkintertable import TableCanvas, TableModel


"""Created a sudoku class which has tkinter interface
TODO:Making a board layout first """

class Sudoku:

    def __init__(self):
        #creating a root window
        self.root=tk.Tk()
        self.root.title("Smart Sudoku")

       
        self.root.geometry("800x800")


        self.menubar=tk.Menu(self.root)
        self.filemenu=tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Close",command=exit)
        self.menubar.add_cascade(menu=self.filemenu,label="File")
        self.root.config(menu=self.menubar)
        


        self.label=tk.Label(self.root,text="Smart Sudoku",font=('Arial',30))
        self.label.pack(padx=10,pady=10)

        button_frame=tk.Frame(self.root)

        
        #this configuration depends on the number of columns we want to have in the grid 
        #this creates the configuration for 9 different columns at the board
        for i in range(9):
            button_frame.columnconfigure(i,weight=1)
            
        
        buttons= [[0 for i in range(9)] for j in range(9)]

       
        for i in range(9):
            for j in range(9):
                buttons[i][j]=tk.Button(button_frame,text=f"{i},{j}",width=1,height=4)
                buttons[i][j].grid(row=i,column=j,sticky=tk.W+tk.E)
        
        button_frame.pack(fill="x",padx=10,pady=20)

                

    
        self.root.mainloop()

    
        




Sudoku()
