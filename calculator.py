import tkinter as tk

#JaayEssencee
#must run program from buttonBindings to work

#displays a black, resizeable screen
root = tk.Tk()
root.title("Calculator Project: Intro To CompSci")
root.config(bg = "black")
root.geometry("730x630")
root.resizable(False, False)
#
from tkinter import ttk
#
label = tk.Label(root, text = "Jaay's Calc", bg = "black")
label.pack(anchor = tk.W, expand = True, fill = tk.BOTH)
#import button bindings
import buttonBindings
#window
window = ttk.Frame(root, width = 730, height = 30, border = 2, relief = "sunken")
window.pack(anchor = tk.N)
#window input
windowDisplay = tk.Entry(window, font = ("Georgia", 16, "bold"), textvariable = buttonBindings.windowInput, width = 50, justify = "right")
windowDisplay.grid(row = 0, column = 0)
windowDisplay.pack(ipady = 10)
#frame
frame = ttk.Frame(root, width = 730, height = 500, border = 6, relief = "sunken")
frame.pack(anchor = tk.W, expand = True, fill = tk.BOTH)
#buttons
#top row
percentButton = tk.Button(frame, text = "%", font = ("Georgia", 14),width = 12, height = 6, command = lambda : buttonBindings.click("%"))
percentButton.grid(row = 1, column = 0, sticky = "w")

squareRootButton = tk.Button(frame, text = "√", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("√"))
squareRootButton.grid(row = 1, column = 1, sticky = "w")

exponentButton = tk.Button(frame, text = "^", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("^"))
exponentButton.grid(row = 1, column = 2, sticky = "w")

plusButton = tk.Button(frame, text = "+", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("+"))
plusButton.grid(row = 1, column = 3, sticky = "w")

minusButton = tk.Button(frame, text = "-", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("-"))
minusButton.grid(row = 1, column = 4, sticky = "w")
#2nd row
fractionButton = tk.Button(frame, text = "x/y", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.doubleClick("x", "y"))
fractionButton.grid(row = 2, column = 0, sticky = "w")

zeroButton = tk.Button(frame, text = "()", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("0"))
zeroButton.grid(row = 2, column = 1, sticky = "w")

parenthesisButton = tk.Button(frame, text = "(  )", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.doubleClick("(", ")"))
parenthesisButton.grid(row = 2, column = 2, sticky = "w")

divideButton = tk.Button(frame, text = "÷", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("÷"))
divideButton.grid(row = 2, column = 3, sticky = "w")

multiplyButton = tk.Button(frame, text = "x", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("x"))
multiplyButton.grid(row = 2, column = 4, sticky = "w")
#3rd row
sevenButton = tk.Button(frame, text = "7", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("7"))
sevenButton.grid(row = 3, column = 0, sticky = "w")

eightButton = tk.Button(frame, text = "8", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("8"))
eightButton.grid(row = 3, column = 1, sticky = "w")

nineButton = tk.Button(frame, text = "9", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("9"))
nineButton.grid(row = 3, column = 2, sticky = "w")

posNegButton = tk.Button(frame, text = "+/-", font = ("Georgia", 14), width = 28, height = 6, command = lambda : buttonBindings.doubleClick("+", "-"))
posNegButton.grid(row = 3, column = 3, sticky = "w", columnspan = 2)
#4th row
fourButton = tk.Button(frame, text = "4", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("4"))
fourButton.grid(row = 4, column = 0, sticky = "w")

fiveButton = tk.Button(frame, text = "5", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("5"))
fiveButton.grid(row = 4, column = 1, sticky = "w")

sixButton = tk.Button(frame, text = "6", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("6"))
sixButton.grid(row = 4, column = 2, sticky = "w")

pointButton = tk.Button(frame, text = ".", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("."))
pointButton.grid(row = 4, column = 3, sticky = "w")

equalButton = tk.Button(frame, text = "=", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.equal())
equalButton.grid(row = 4, column = 4, sticky = "w")
#bottom row
oneButton = tk.Button(frame, text = "1", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("1"))
oneButton.grid(row = 5, column = 0, sticky = "w")

twoButton = tk.Button(frame, text = "2", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("2"))
twoButton.grid(row = 5, column = 1, sticky = "w")

threeButton = tk.Button(frame, text = "3", font = ("Georgia", 14), width = 12, height = 6, command = lambda : buttonBindings.click("3"))
threeButton.grid(row = 5, column = 2, sticky = "w")

clearButton = tk.Button(frame, text = "CLEAR", font = ("Georgia", 14), width = 28, height = 6, command = lambda : buttonBindings.clear())
clearButton.grid(row = 5, column = 3, sticky = "w", columnspan = 2)
#buttons
#
root.mainloop()