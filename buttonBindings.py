import tkinter
from tkinter import *
import calculator

windowInput = StringVar()

def click(item) :
    windowInput.set(item)
    #global expression
    #expression = windowInput + windowInput(item)
    
def doubleClick(item1, item2) :
    windowInput.set(item1)
    windowInput.set(item2)

def clear() :
    #global expression
    #expression = ""
    windowInput.set("")

def equal() :
    global expression

def evaluate() :
    result = windowInput(evaluate(expression)) 
    windowInput.set(result)
    #expression = ""

#buttons
#command = lamda : buttonBindings.click("%")