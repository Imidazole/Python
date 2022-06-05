from math import factorial

def fact(n):
	for i in range(1, n + 1):
		yield (i, factorial(i))

n = int(input("Введите целое число:\n"))

for (i, f) in fact(n):
	print(f"{i}! = {f}")
