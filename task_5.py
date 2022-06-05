from functools import reduce

def mult(a, b):
	return a * b

l = [el for el in range(100, 1001) if el % 2 == 0]

m = reduce(mult, l)

print(m)
