import tkinter as tk

#JaayEssencee

#displays a black, resizeable screen
root = tk.Tk()
root.title("Calculator Project: Intro To CompSci")
root.config(bg = "black")
root.geometry("600x400")
root.resizable(True, True)
#
label = tk.Label(root, text = "Jaay's Calc", bg = "black")
label.pack(anchor = tk.W, expand = True, fill = tk.BOTH)

from tkinter import ttk
frame = ttk.Frame(root, width = 400, height = 200, border = 6, relief = "sunken")
frame.pack(anchor = tk.W, expand = True, fill = tk.BOTH)
#buttons
percentButton = tk.Button(frame, text = "%", font = ("Georgia", 14),width = 20, height = 10)
percentButton.grid(row = 0, column = 0, sticky = "w")
#
root.mainloop()