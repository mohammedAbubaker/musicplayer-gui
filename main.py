import tkinter as tk
import tkinter as tk					 
from tkinter import ttk 


root = tk.Tk() 
root.title("Music Player") 
tabControl = ttk.Notebook(root) 

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl) 

tabControl.add(tab1, text ='Artists') 
tabControl.add(tab2, text ='Albums') 
tabControl.add(tab3, text ='Songs') 

tabControl.pack(expand = 1, fill ="both") 

root.mainloop() 
