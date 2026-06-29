import random
import string
from tkinter import *

def generate():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(int(length.get())))
    output.delete(0, END)
    output.insert(0, password)

root = Tk()
root.title("Password Generator")
root.geometry("350x220")

Label(root,text="Password Length",font=("Arial",12)).pack(pady=10)

length = Entry(root,font=("Arial",14))
length.pack()

Button(root,text="Generate Password",command=generate).pack(pady=15)

output = Entry(root,font=("Arial",14),width=30)
output.pack()

root.mainloop()
