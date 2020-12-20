from tkinter import *
import check

check.possible_moves = []

WIDTH = 800
HEIGHT = 800

root = Tk()
root.title('Chess')
root.minsize(WIDTH, HEIGHT)
canv = Canvas(width = WIDTH, height = HEIGHT, bg = 'peach puff')
canv.pack()

'''
Фигуры и обозначения к ним
Пешка - P
Король - K
Королева - Q
Ладья - L
Слон - S
Конь - H
W или B в конце - цвет фигуры
'''
field = [
	['LB', 'HB', 'SB', 'QB', 'KB', 'SB', 'HB', 'LB'],
	['PB', 'PB', 'PB', 'PB', 'PB', 'PB', 'PB', 'PB'],
	['', '', '', '', '', '', '', ''],
	['', '', '', '', '', '', '', ''],
	['', '', '', '', '', '', '', ''],
	['', '', '', '', '', '', '', ''],
	['PW', 'PW', 'PW', 'PW', 'PW', 'PW', 'PW', 'PW'],
	['LW', 'HW', 'SW', 'QW', 'KW', 'SW', 'HW', 'LW']
]

def exit_f():
	exit(0)

def draw(field):
	canv.delete('all')
	for x in range(8):
		for y in range(8):
			if x % 2 != y % 2:
				#black
				canv.create_rectangle(x * 100, y * 100, x * 100 + 100, y * 100 + 100, fill = 'tan4')
			if field[y][x] == 'LW':
				figure = '♖'
			elif field[y][x] == 'HW':
				figure = '♘'
			elif field[y][x] == 'SW':
				figure = '♗'
			elif field[y][x] == 'KW':
				figure = '♔'
			elif field[y][x] == 'QW':
				figure = '♕'
			elif field[y][x] == 'PW':
				figure = '♙'
			elif field[y][x] == 'LB':
				figure = '♜'
			elif field[y][x] == 'HB':
				figure = '♞'
			elif field[y][x] == 'SB':
				figure = '♝'
			elif field[y][x] == 'KB':
				figure = '♚'
			elif field[y][x] == 'QB':
				figure = '♛'
			elif field[y][x] == 'PB':
				figure = '♟'
			else:
				figure = ''
			canv.create_text((x * 100 + 50, y * 100 + 50), font = ('Purisa', 30), text = figure)
draw(field)

def click(event):
	cell_x = event.x // 100
	cell_y = event.y // 100
	print(f'Click. Sell : {cell_y}:{cell_x}. Figure: {field[cell_y][cell_x]}')
	
	if check.possible_moves == [] and field[cell_y][cell_x] != '' and field[cell_y][cell_x][-1] == check.flag:
		p_m = check.moves(field, field[cell_y][cell_x], cell_y, cell_x)
		check.possible_moves = p_m
		#print(check.possible_moves)
		for move in check.possible_moves[:-2]:
			canv.create_rectangle((move[1] * 100 + 40, move[0] * 100 + 40, move[1] * 100 + 60, move[0] * 100 + 60),
								fill = 'cyan')

	elif check.possible_moves != []:
		if [cell_y, cell_x] in check.possible_moves:
			x = check.possible_moves[-2][0]
			y = check.possible_moves[-2][1]
			if cell_y == x and cell_x == y:
				pass
			else:
				field[cell_y][cell_x] = field[x][y]
				field[x][y] = ''
				check.possible_moves = []
				draw(field)
				if check.flag == 'W':
					check.flag = 'B'
				else:
					check.flag = 'W'
				fW = False
				fB = False
				for line in field:
					for el in line:
						if el == 'KW':
							fW = True
						if el == 'KB':
							fB = True
				if not fW:
					canv.delete('all')
					canv.create_text((360, 360), text = 'Black win')
					root.after(1000, exit_f)
				if not fB:
					canv.delete('all')
					canv.create_text((360, 360), text = 'White win')
					root.after(1000, exit_f)
		else:
			check.possible_moves = []
			draw(field)

root.bind('<Button-1>', click)

root.mainloop()