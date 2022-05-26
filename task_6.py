reven = float(input("Введите выручку компании:\n"))
expen = float(input("Введите издержки компании:\n"))

profit = reven - expen

if (reven > expen):
	rent = profit / reven
	print("Рентабельность выручки:", rent, sep = "\n")
	
	person = int(input("Введите численность сотрудников фирмы:\n"))
	
	profpp = profit / person
	
	print("Прибыль фирмы в расчёте на одного сотрудника:", profpp, sep = "\n")
