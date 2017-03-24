'''
n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print('END')
'''

n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:
	#judge even or not
		continue
	print(n)
