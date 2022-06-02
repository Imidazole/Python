res = 0
br = 0

while br == 0:
	s = input("Введите строку с числами. Для завершения работы введите 'q':\n")
	arr = s.split()
	if "q" in arr:
		br = 1
		arr.remove("q")
	r = list(map(int, arr))
	for el in r:
		res += el
	print("Сумма чисел:", res, sep = "\n")
