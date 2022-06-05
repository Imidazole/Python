from itertools import count

i = input("Введите начальное значение:\n")

for el in count(3):
	if el > 1000:
		break
	else:
		print(el)
