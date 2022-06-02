def my_func(a, b, c):
	if a < b:
		a, b = b, a
	if b < c:
		b, c = c, b
	if a < b:
		a, b = b, a
	return a + b

a = int(input())
b = int(input())
c = int(input())

print(my_func(a, b, c))
