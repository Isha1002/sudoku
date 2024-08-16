import tkinter as tk 

root=tk.Tk()
root.geometry("500x500")
root.title("My tkinter practice")


label=tk.Label(root,text="Welcome to this program",font=('Tahoma',18))
label.pack(padx=20,pady=20)

textbox=tk.Text(root,height=5,font=('Arial',14))
textbox.pack(padx=10,pady=30)

button=tk.Button(root,text="Click here",font=('Arial',18))
button.pack(padx=10)

button_frame=tk.Frame(root)
#this configuration depends on the number of rows we have 
button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)

btn1=tk.Button(button_frame,text="1",font=('Arial',18))
btn1.grid(row=1,column=0,sticky=tk.W+tk.E)
btn2=tk.Button(button_frame,text="2",font=('Arial',18))
btn2.grid(row=1,column=1,sticky=tk.W+tk.E)
btn3=tk.Button(button_frame,text="3",font=('Arial',18))
btn3.grid(row=2,column=0,sticky=tk.W+tk.E)
btn4=tk.Button(button_frame,text="4",font=('Arial',18))
btn4.grid(row=2,column=1,sticky=tk.W+tk.E)

button_frame.pack(fill='x')
root.mainloop()