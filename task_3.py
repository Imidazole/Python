class InpNotNumericExc(Exception):
	def __init__(self, txt):
		pass

print("Введите числа. Для окончания ввода введите пустую строку")
l = []

while(True):
	inp = input()
	if inp == "":
		break
	try:
		if inp.isnumeric():
			l.append(inp)
		else:
			raise(InpNotNumericExc("Строка '" + inp + "' не является корректно записанным числом."))
	except InpNotNumericExc as err:
		print(err)

print("Введённые числа: ", " ".join(l), sep = "\n")
