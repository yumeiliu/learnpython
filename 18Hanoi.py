# -*- coding: utf-8 -*-

def move(n, a, b, c):
	if(n == 1):
		print('move', a, '-->', c)
		return

	move(n-1, a, c, b)
	print('move', a, '-->', c)
	move(n-1, b, a, c)


n = int(input())

move(n, 'A', 'B', 'C')
