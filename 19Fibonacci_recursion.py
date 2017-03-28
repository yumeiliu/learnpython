# -*- coding: utf-8 -*-

def sequence(n):
	if n==1 or n==2:
		return 1
	else:
		return sequence(n-1) + sequence(n-2)

x = int(input())

s = sequence(x)
print(s)
