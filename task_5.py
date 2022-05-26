reven = int(input("Введите выручку компании:\n"))
expen = int(input("Введите издержки компании:\n"))

if (reven > expen):
	print("Прибыль - выручка больше издержек")
elif (reven == expen):
	print("Выручка равна издержкам")
else:
	print("Убыток - издержки больше выручки")
