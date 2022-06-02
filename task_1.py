def division(n, d):
	try:
		return n / d
	except ZeroDivisionError:
		return "На ноль делить нельзя!"

a = float(input("Введите делимое:\n"))
b = float(input("Введите делитель:\n"))

res = division(a, b)

print("Результат деления:", res, sep = "\n")
