import tkinter as tk

#JaayEssencee

#displays a black, resizeable screen
root = tk.Tk()
root.title("Calculator Project: Intro To CompSci")
root.config(bg = "black")
root.geometry("730x575")
root.resizable(False, False)
#import button bindings
#import buttonBindings
#
label = tk.Label(root, text = "Jaay's Calc", bg = "black")
label.pack(anchor = tk.W, expand = True, fill = tk.BOTH)
#frame
from tkinter import ttk
frame = ttk.Frame(root, width = 730, height = 500, border = 6, relief = "sunken")
frame.pack(anchor = tk.W, expand = True, fill = tk.BOTH)
#buttons
#top row
percentButton = tk.Button(frame, text = "%", font = ("Georgia", 14),width = 12, height = 6)
percentButton.grid(row = 0, column = 0, sticky = "w")

squareRootButton = tk.Button(frame, text = ",-", font = ("Georgia", 14), width = 12, height = 6)
squareRootButton.grid(row = 0, column = 1, sticky = "w")

exponentButton = tk.Button(frame, text = "^", font = ("Georgia", 14), width = 12, height = 6)
exponentButton.grid(row = 0, column = 2, sticky = "w")

plusButton = tk.Button(frame, text = "+", font = ("Georgia", 14), width = 12, height = 6)
plusButton.grid(row = 0, column = 3, sticky = "w")

minusButton = tk.Button(frame, text = "-", font = ("Georgia", 14), width = 12, height = 6)
minusButton.grid(row = 0, column = 4, sticky = "w")
#2nd row
fractionButton = tk.Button(frame, text = "x/y", font = ("Georgia", 14), width = 12, height = 6)
fractionButton.grid(row = 1, column = 0, sticky = "w")

openParenthesisButton = tk.Button(frame, text = "(", font = ("Georgia", 14), width = 12, height = 6)
openParenthesisButton.grid(row = 1, column = 1, sticky = "w")

closedParenthesisButton = tk.Button(frame, text = ")", font = ("Georgia", 14), width = 12, height = 6)
closedParenthesisButton.grid(row = 1, column = 2, sticky = "w")

divideButton = tk.Button(frame, text = "/", font = ("Georgia", 14), width = 12, height = 6)
divideButton.grid(row = 1, column = 3, sticky = "w")

multiplyButton = tk.Button(frame, text = "x", font = ("Georgia", 14), width = 12, height = 6)
multiplyButton.grid(row = 1, column = 4, sticky = "w")
#3rd row
sevenButton = tk.Button(frame, text = "7", font = ("Georgia", 14), width = 12, height = 6)
sevenButton.grid(row = 2, column = 0, sticky = "w")

eightButton = tk.Button(frame, text = "8", font = ("Georgia", 14), width = 12, height = 6)
eightButton.grid(row = 2, column = 1, sticky = "w")

nineButton = tk.Button(frame, text = "9", font = ("Georgia", 14), width = 12, height = 6)
nineButton.grid(row = 2, column = 2, sticky = "w")

posNegButton = tk.Button(frame, text = "+/-", font = ("Georgia", 14), width = 28, height = 6)
posNegButton.grid(row = 2, column = 3, sticky = "w", columnspan = 2)
#4th row
fourButton = tk.Button(frame, text = "4", font = ("Georgia", 14), width = 12, height = 6)
fourButton.grid(row = 3, column = 0, sticky = "w")

fiveButton = tk.Button(frame, text = "5", font = ("Georgia", 14), width = 12, height = 6)
fiveButton.grid(row = 3, column = 1, sticky = "w")

sixButton = tk.Button(frame, text = "6", font = ("Georgia", 14), width = 12, height = 6)
sixButton.grid(row = 3, column = 2, sticky = "w")

pointButton = tk.Button(frame, text = ".", font = ("Georgia", 14), width = 12, height = 6)
pointButton.grid(row = 3, column = 3, sticky = "w")

equalButton = tk.Button(frame, text = "=", font = ("Georgia", 14), width = 12, height = 6)
equalButton.grid(row = 3, column = 4, sticky = "w")
#bottom row
oneButton = tk.Button(frame, text = "1", font = ("Georgia", 14), width = 12, height = 6)
oneButton.grid(row = 4, column = 0, sticky = "w")

twoButton = tk.Button(frame, text = "2", font = ("Georgia", 14), width = 12, height = 6)
twoButton.grid(row = 4, column = 1, sticky = "w")

threeButton = tk.Button(frame, text = "3", font = ("Georgia", 14), width = 12, height = 6)
threeButton.grid(row = 4, column = 2, sticky = "w")

clearButton = tk.Button(frame, text = "CLEAR", font = ("Georgia", 14), width = 28, height = 6)
clearButton.grid(row = 4, column = 3, sticky = "w", columnspan = 2)
#buttons
#
root.mainloop()