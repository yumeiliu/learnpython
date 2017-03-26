# -*- coding: utf-8 -*-
# recursion

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

print("请输入阶乘的阶数：")
s = int(input())

print(fact(s))
