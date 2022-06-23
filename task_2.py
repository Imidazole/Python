class ManualZeroDivExc(Exception):
	def __init__(self, txt):
		self.txt = txt
	
a = int(input("Введите делимое:\n"))
b = int(input("Введите делитель:\n"))

try:
	if b == 0:
		raise ManualZeroDivExc("На ноль делить нельзя!")
	else:
		print("Результат: ", a / b)
except ManualZeroDivExc as err:
	print(err)

