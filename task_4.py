s = input("Введите строку:\n")

for i, el in enumerate(s.split()):
	print("{}-е слово:".format(i), el[0 : 10])
