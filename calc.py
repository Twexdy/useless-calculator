from tkinter import *

# root configs
root = Tk()
root.title("world's worst calculator")
root.iconbitmap("icon.ico")
root.resizable(False,False)


# functions
def addItem(item):
     current = numberDisplay.get()
     clear()
     numberDisplay.insert(0, f"{current}{item}")


def backspace():
     current = numberDisplay.get()
     numberDisplay.delete(len(current) - 1, END)
    

def clear():
    numberDisplay.delete(0, END)
    

def equalFunction():
    try:
        result = eval(numberDisplay.get())
        clear()
        numberDisplay.insert(0, result)
    except:
        clear()
        numberDisplay.insert(0, "Error. Press 'clear'")


# number bar
numberDisplay = Entry(root, width=25, borderwidth=5, font=20)
numberDisplay.grid(row=0, column=0, columnspan=3, padx=5, pady=20)

# number buttons
Button(text="1", width=13, height=5, command=lambda:addItem("1")).grid(row=2, column=0, padx=1, pady=1)
Button(text="2", width=13, height=5, command=lambda:addItem("2")).grid(row=2, column=1, padx=1, pady=1)
Button(text="3", width=13, height=5, command=lambda:addItem("3")).grid(row=2, column=2, padx=1, pady=1)
Button(text="4", width=13, height=5, command=lambda:addItem("4")).grid(row=3, column=0, padx=1, pady=1)
Button(text="5", width=13, height=5, command=lambda:addItem("5")).grid(row=3, column=1, padx=1, pady=1)
Button(text="6", width=13, height=5, command=lambda:addItem("6")).grid(row=3, column=2, padx=1, pady=1)
Button(text="7", width=13, height=5, command=lambda:addItem("7")).grid(row=4, column=0, padx=1, pady=1)
Button(text="8", width=13, height=5, command=lambda:addItem("8")).grid(row=4, column=1, padx=1, pady=1)
Button(text="9", width=13, height=5, command=lambda:addItem("9")).grid(row=4, column=2, padx=1, pady=1)
Button(text="0", width=13, height=5, command=lambda:addItem("0")).grid(row=5, column=1, padx=1, pady=1)
Button(text=".", width=7, height=3, command=lambda:addItem(".")).grid(row=5, column=0, padx=2, pady=2)

# operator buttons (* / + - = del clear)
Button(text="+", width=6, height=5, command=lambda:addItem("+")).grid(row=2, column=3, padx=13,)
Button(text="-", width=6, height=5, command=lambda:addItem("-")).grid(row=3, column=3, padx=13,)
Button(text="*", width=6, height=5, command=lambda:addItem("*")).grid(row=4, column=3, padx=13,)
Button(text="/", width=6, height=5, command=lambda:addItem("/")).grid(row=5, column=3, padx=13,)
Button(text="=", width=8, height=5, command=equalFunction).grid(row=2, column=4, padx=5)
Button(text="del", width=8, height=5, command=backspace).grid(row=3, column=4, padx=5)
Button(text="clear", width=8, height=5, command=clear).grid(row=4, column=4, padx=5,)

root.mainloop()
