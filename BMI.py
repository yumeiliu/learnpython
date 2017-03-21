# -*- coding: utf-8 -*-

#Judge someone's BMI

print('请输入你的身高：')
h = input()

print('请输入你的体重：')
w = input()

#bmi = int(w) / (int(h) * int(h))
bmi = float(w) / (float(h) * float(h))

'''
1. 求x的n次方，python内置操作符**
>>>x**n
2. 注意：输入的身高、体重不是整数，不能用int()转换
'''

if bmi < 18.5:
	print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')
