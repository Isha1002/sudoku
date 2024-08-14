
from tkinter import ttk
from tkinter import *
from tkintertable import TableCanvas, TableModel


root=Tk()
"""
frm=ttk.Frame(root,padding=500)
frm.grid()
ttk.Label(frm,text="Sudoku").grid(row=0,column=0)
ttk.Button(frm,text="Quit",command=root.destroy).grid(row=1, column=0)
"""
tframe = ttk.Frame(root,padding =200)
tframe.pack()

table = TableCanvas(tframe,rows=row,cols=col,height=200,width=500)

        
        

table.show()
root.mainloop()
