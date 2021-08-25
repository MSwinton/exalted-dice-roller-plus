from approller import Roller
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Exalted Dice Roller Plus")
root.geometry('400x200')


content = ttk.Frame(root, padding="10 10")
content.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
instructions = ttk.Label(content, text = "how many dice do you want to roll?")
instructions.pack()


def roll_it():
    roller = Roller()
    
    output1 ['text'] = roller.roll_dice(int(entry1.get()))



entry1 = Entry(content, width = 20)
entry1.pack()


roll_button = Button(content, text="do it", command=roll_it)
roll_button.pack()

output2 = Label(content, text='Your roll:')
output2.pack()
output1 = Label(content, text=' ', justify="center", wraplength=350)
output1.pack()

root.mainloop()
