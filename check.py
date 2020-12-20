possible_moves = []
flag = 'W'


def moves(field, figure, x, y):
	m = []

	if figure[0] == 'H':
		m = [[x - 2, y + 1], [x - 2, y - 1],
			 [x - 1, y - 2], [x + 1, y - 2],
			 [x + 2, y + 1], [x + 2, y - 1],
			 [x - 1, y + 2], [x + 1, y + 2]]
	
	if figure[0] == 'L' or figure[0] == 'Q':
		a = x - 1
		b = y
		while a >= 0:
			if field[a][b] == '':
				m.append([a, b])
			elif field[a][b][-1] != field[x][y][-1]:
				m.append([a, b])
				break
			else:
				break
			a -= 1
		a = x + 1
		b = y
		while a <= 7:
			if field[a][b] == '':
				m.append([a, b])
			elif field[a][b][-1] != field[x][y][-1]:
				m.append([a, b])
				break
			else:
				break
			a += 1
		a = x
		b = y + 1
		while b <= 7:
			if field[a][b] == '':
				m.append([a, b])
			elif field[a][b][-1] != field[x][y][-1]:
				m.append([a, b])
				break
			else:
				break
			b += 1
		a = x
		b = y - 1
		while b >= 0:
			if field[a][b] == '':
				m.append([a, b])
			elif field[a][b][-1] != field[x][y][-1]:
				m.append([a, b])
				break
			else:
				break
			b -= 1

	if figure[0] == 'S' or figure[0] == 'Q':
		a = x + 1
		b = y + 1
		while a <= 7 and b <= 7:
			if field[a][b] == '':
				m.append([a, b])
			elif field[a][b][-1] != field[x][y][-1]:
				m.append([a, b])
				break
			else:
				break
			a += 1
			b += 1
		a = x + 1
		b = y - 1
		while a <= 7 and b >= 0:
			if field[a][b] == '':
				m.append([a, b])
			elif field[a][b][-1] != field[x][y][-1]:
				m.append([a, b])
				break
			else:
				break
			a += 1
			b -= 1
		a = x - 1
		b = y + 1
		while a >= 0 and b <= 7:
			if field[a][b] == '':
				m.append([a, b])
			elif field[a][b][-1] != field[x][y][-1]:
				m.append([a, b])
				break
			else:
				break
			a -= 1
			b += 1
		a = x - 1
		b = y - 1
		while a >= 0 and b >= 0:
			if field[a][b] == '':
				m.append([a, b])
			elif field[a][b][-1] != field[x][y][-1]:
				m.append([a, b])
				break
			else:
				break
			a -= 1
			b -= 1

	if figure[0] == 'K':
		m = [
			[x + 1, y], [x, y + 1],
			[x + 1, y + 1], [x - 1, y - 1],
			[x - 1, y], [x, y - 1],
			[x - 1, y + 1], [x + 1, y - 1]
		]

	if figure[0] == 'P':
		if figure[1] == 'W':
			if x == 6:
				m = [[x - 1, y], [x - 2, y]]
			else:
				m = [[x - 1, y]]
			for po_m in m:
				po_x = po_m[0]
				po_y = po_m[1]
				if field[po_x][po_y] != '':
					m.remove(po_m)
			if x - 1 >= 0 and y + 1 <= 7 and field[x - 1][y + 1] != '':
				m.append([x - 1, y + 1])
			if x - 1 >= 0 and y - 1 >= 0 and field[x - 1][y - 1] != '':
				m.append([x - 1, y - 1])

		if figure[1] == 'B':
			if x == 1:
				m = [[x + 1, y], [x + 2, y]]
			else:
				m = [[x + 1, y]]
			for po_m in m:
				po_x = po_m[0]
				po_y = po_m[1]
				if field[po_x][po_y] != '':
					m.remove(po_m)
			if x + 1 <= 7 and y + 1 <= 7 and field[x + 1][y + 1] != '':
				m.append([x + 1, y + 1])
			if x + 1 <= 7 and y - 1 >= 0 and field[x + 1][y - 1] != '':
				m.append([x + 1, y - 1])

	correct_moves = []
	for p_move in m:
		a = p_move[0]
		b = p_move[1]
		if a >= 0 and a <= 7 and b >= 0 and b <= 7:
			if field[a][b] == '':
				correct_moves.append([a, b])
			elif field[x][y][-1] != field[a][b][-1]:
				correct_moves.append([a, b])
	correct_moves.append([x, y])
	correct_moves.append(figure[-1])
	return correct_moves