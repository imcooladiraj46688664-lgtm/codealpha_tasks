from tkinter import *

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = Tk()
root.title("To-Do List")
root.geometry("400x450")

task_entry = Entry(root,font=("Arial",14),width=25)
task_entry.pack(pady=15)

Button(root,text="Add Task",command=add_task,width=20).pack()

listbox = Listbox(root,font=("Arial",13),width=35,height=12)
listbox.pack(pady=15)

Button(root,text="Delete Selected",command=delete_task,width=20).pack()

root.mainloop()
