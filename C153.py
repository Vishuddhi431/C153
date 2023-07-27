#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 07:43:16 2023

@author: vishuddhimakeshwaran
"""

from tkinter import *
import random 

root = Tk()
root.geometry("400x500")
root.title("Password Generator")

label = Label(root)

entry1 = Entry(root)

array1 = [[["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], 
           ["head", "Tail", "Cat", "dog"], 
           ["A", "B", "C", "D", "E", "F", "G"], 
           ["!", "@", "#", "$", "%", "^", "&", "*"]]]

print(array1)

def gen(): 
    no1 = random.randint(0, 9)
    no2 = random.randint(0, 3)
    no3 = random.randint(0, 6)
    no4 = random.randint(0, 9)
    no5 = random.randint(0, 9)
    no6 = random.randint(0, 7)
    
    password = entry1.get() + array1[0][0][no1] + array1[0][0][no4] + array1[0][0][no5] + array1[0][1][no2] + array1[0][2][no3] + array1[0][3][no6]
    
    label["text"] = password
    
button1 = Button(root, text = "Generate Password", command = gen)
button1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
entry1.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()

