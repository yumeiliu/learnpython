# -*- coding: utf-8 -*-

def powern(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

'''
def power(x):
	return x*x
''' 

print(powern(5))
print(powern(5, 5))

