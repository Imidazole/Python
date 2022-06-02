def my_func(x, y):
	y *= -1
	res = 1
	while y > 0:
		res *= x
		y -= 1
	res = 1 / res
	return res

x = float(input("Введите x:\n"))	
y = int(input("Введите y:\n"))

print(my_func(x, y))
