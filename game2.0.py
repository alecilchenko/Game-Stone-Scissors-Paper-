import tkinter as tk
from tkinter import ttk
import random
from PIL import ImageTk, Image

def win():
	label_game_res['text'] = 'You won'
	temp = int(player.get()) + 1
	player.set(temp)
	

def game(arg, photo):
	choice = random.choice(list(comp_choice.keys()))
	label_g1['image'] = photo
	label_g2['image'] = comp_choice[choice]
	if arg == choice:
		#это ничья
		label_game_res['text'] = 'Dead heat'
	elif arg == 'Stone' and (choice == 'Scissors' or choice == 'Lizard'):
		#это победа игрока
		win()
	elif arg == 'Lizard' and (choice == 'Spok' or choice == 'Paper'):
		win()
	elif arg == 'Spok' and (choice == 'Scissore' or choice == 'Stone'):
		win()
	elif arg == 'Scissore' and (choice == 'Lizard' or choice == 'Paper'):
		win()
	elif arg == 'Paper' and (choice == 'Spok' or choice == 'Stone'):
		win()
	else:
		#Проиграл
		label_game_res['text'] = 'You lose'
		temp = int(comp.get()) + 1
		comp.set(temp)



root = tk.Tk()


stone_img = ImageTk.PhotoImage(Image.open("stone.png"))
scis_img = ImageTk.PhotoImage(Image.open("scissore.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
spok_img = ImageTk.PhotoImage(Image.open("spok.png"))
lizard_img = ImageTk.PhotoImage(Image.open("lizard.png"))

comp_choice = {'Stone':stone_img, 'Scissors':scis_img, 'Paper':paper_img, 'Spok': spok_img, 'Lizard':lizard_img}

#Создаем необходимые элементы
#Frame с двумя label и lable результат, пять кнопок, lable - Результат, два lable - количество побед

board = ttk.Frame(root)
label_g1 = ttk.Label(board)
label_g2 = ttk.Label(board)
label_game_res = ttk.Label(board)

bt1 = ttk.Button(root, image=stone_img, command=lambda:game('Stone', stone_img))
bt2 = ttk.Button(root, image=scis_img, command=lambda:game('Scissors', scis_img))
bt3 = ttk.Button(root, image=paper_img, command=lambda:game('Paper', paper_img))
bt4 = ttk.Button(root, image=spok_img, command=lambda:game('Spok', spok_img))
bt5 = ttk.Button(root, image=lizard_img, command=lambda:game('Lizard', lizard_img))

label_resolt = ttk.Label(root, text='Score')
player = tk.StringVar()
player.set('0')
label_player = ttk.Label(root, textvariable=player)
comp = tk.StringVar()
comp.set('0')
label_comp = ttk.Label(root, textvariable=comp)

#Расположим элементы

board.grid(row=1, column=1, columnspan=5)
label_game_res.grid(row=1, column=1, columnspan=2)
label_g1.grid(row=2, column=1)
label_g2.grid(row=2, column=2)

bt1.grid(row=2, column=1)
bt2.grid(row=2, column=2)
bt3.grid(row=2, column=3)
bt4.grid(row=2, column=4)
bt5.grid(row=2, column=5)

label_resolt.grid(row=3, column=1, columnspan=5)
label_player.grid(row=4, column=2)
label_comp.grid(row=4, column=4)

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
board.columnconfigure(1, weight=1)
board.rowconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)


root.mainloop()
