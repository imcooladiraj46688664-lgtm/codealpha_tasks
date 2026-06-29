from tkinter import *

def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Calculator")
root.geometry("320x420")

entry = Entry(root, font=("Arial", 20), bd=8, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
('7',1,0),('8',1,1),('9',1,2),('/',1,3),
('4',2,0),('5',2,1),('6',2,2),('*',2,3),
('1',3,0),('2',3,1),('3',3,2),('-',3,3),
('0',4,0),('.',4,1),('=',4,2),('+',4,3)
]

for (text,row,col) in buttons:
    if text=="=":
        Button(root,text=text,width=8,height=3,command=calculate).grid(row=row,column=col)
    else:
        Button(root,text=text,width=8,height=3,command=lambda t=text:click(t)).grid(row=row,column=col)

Button(root,text="Clear",width=35,height=2,command=clear).grid(row=5,column=0,columnspan=4)

root.mainloop()
