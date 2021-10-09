import random
import tkinter as tk

root=tk.Tk()
root.geometry("700x450")

l1=tk.Label(root,font=("Times",200))

def roll():
	number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	l1.config(text=f'{random.choice(number)}{random.choice(number)}')
	l1.pack()

b1=tk.Button(root,text="ROLL IT",command=roll)
b1.place(x=320,y=0)

root.mainloop()