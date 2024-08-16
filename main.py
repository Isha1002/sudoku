import tkinter as tk
from tkinter import messagebox
class MyGUI:
    def __init__(self):

        self.root=tk.Tk()
        self.menubar=tk.Menu(self.root)
        self.filemenu=tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Close",command=self.closed_window)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Force Quit",command=exit)
        self.filemenu.add_separator()

        self.actionmenu=tk.Menu(self.menubar,tearoff=0)
        self.actionmenu.add_command(label="Display",command=self.show_message)
        
        self.menubar.add_cascade(menu=self.actionmenu,label="Display")
        self.menubar.add_cascade(menu=self.filemenu,label="File")

        self.root.config(menu=self.menubar)

        self.label=tk.Label(self.root,text="Your message",font=('Arial',18))
        self.label.pack(padx=10,pady=10)
        self.textbox=tk.Text(self.root,height=5,font=('Arial',16))
        self.textbox.bind("<KeyPress>",self.shortcut)
        self.textbox.pack(padx=10,pady=10)
        self.check_state=tk.IntVar()
        self.check=tk.Checkbutton(self.root,text="Show message box",font=('Arial',19),variable=self.check_state)
        self.check.pack(padx=10,pady=10)
        self.button=tk.Button(self.root,text="Show message",font=('Arial',18),command=self.show_message)
        self.button.pack(padx=10,pady=10)
        self.clearbtn=tk.Button(self.root,text="Clear",font=('Arial',18),command=self.clear_textbox)
        self.clearbtn.pack(padx=10,pady=10)
        self.root.protocol("WM_DELETE_WINDOW",self.closed_window)

        self.root.mainloop()

    def show_message(self):
        if(self.check_state.get()==0):
            print(self.textbox.get('1.0',tk.END)) #start from beginning to end
        else:
            messagebox.showinfo(title="msg",message=self.textbox.get('1.0',tk.END))

    def shortcut(self,event):
        
        if(event.keysym=="Return"):
            self.show_message()

    def closed_window(self):
        if(messagebox.askyesno(title="Quit?",message="Do you really want to quit?")):
            self.root.destroy()
    def clear_textbox(self):
        self.textbox.delete('1.0',tk.END)


MyGUI()