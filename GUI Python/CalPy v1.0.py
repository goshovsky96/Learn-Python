from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
root = Tk() 
root.title("CalPy v1.0")
bttn_list = [ "C","(", ")","+","9", "8", "7", "-", "6", "5", "4","*", "3","2","1","/",".", "0","√2","xⁿ","n!","sin", "cos","="]
r = 1; c = 0;
for i in bttn_list:
	rel = ""
	cmd=lambda x=i: calc(x)
	ttk.Button(root, text=i, command = cmd, width = 8).grid(row=r, column = c)
	c += 1
	if c >= 4:
		c = 0; r += 1;
calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)
def calc(key):
    global memory
    if key == "=": 
        str1 = "-+0123456789.*/)(" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Введено не правильно перший символ!")
            messagebox.showerror("Error! Вводіть тільки чифри.")
        try: calc_entry.insert(END, "=" + str(eval(calc_entry.get())))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Перевірте ввід на коректність")
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "xⁿ": calc_entry.insert(END, "**")
    elif key == "sin": calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos": calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "(": calc_entry.insert(END, "(")
    elif key == ")": calc_entry.insert(END, ")")
    elif key == "n!": calc_entry.insert(END, "!=" + str(math.factorial(int(calc_entry.get()))))
    elif key == "√2": calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    else:
        if "=" in calc_entry.get(): calc_entry.delete(0, END)
        calc_entry.insert(END, key)
root.mainloop()