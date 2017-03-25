# -*- coding: utf-8 -*-

#calculate quadratic equation

import math

def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
	x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)

	return x1, x2

print("请输入a: ")
a = float(input())
print("请输入b: ")
b = float(input())
print("请输入c: ")
c = float(input())

x1, x2 = quadratic(a, b, c)
print("x1 =",x1,", x2 =",x2)

'''
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
'''
