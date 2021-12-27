import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random


def roll():
	for i in range(int(number.get())):
		im = random.sample(list(dice_dict.keys()), 1)
		board_label = ttk.Label(board, image=im)
		board_label.grid(row=0, column=i)
		

root = tk.Tk()

#Picture of all sides
one_img = ImageTk.PhotoImage(Image.open('1.png'))
two_img = ImageTk.PhotoImage(Image.open('2.png'))
three_img = ImageTk.PhotoImage(Image.open('3.png'))
four_img = ImageTk.PhotoImage(Image.open('4.png'))
five_img = ImageTk.PhotoImage(Image.open('5.png'))
six_img = ImageTk.PhotoImage(Image.open('6.png'))
dice_dict = {one_img : 1, two_img : 2, three_img : 3, four_img : 4, five_img : 5, six_img : 6}

#Create board for dice
board = tk.Canvas(root)
board.grid(row=1, column=1, columnspan=2)


#Create entry for number of dices
e = tk.StringVar()
number = ttk.Entry(root, textvariable=e)
number.grid(row=2, column=1)

#Create button
start_bt = ttk.Button(root, text='Roll the dice', command=roll)
start_bt.grid(row=2, column=2)


root.mainloop()
