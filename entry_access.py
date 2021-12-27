import tkinter as tk
from tkinter import ttk

def print_c():
	print(e.get())


root = tk.Tk()
root.title('Enter password')
root.geometry('300x50+100+100')



#Создаем строку ввода
e = tk.StringVar()
user_input = tk.Entry(root, textvariable=e, show='*')
user_input.pack()


#Создаем кнопку. При нажатии она печатает в консоль значение из строки ввода
bt = tk.Button(text='Enter', command=print_c)
bt.pack()

user_input.focus()

root.mainloop()
