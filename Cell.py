class Cell:
	__n = 0
	
	def __init__(self, n):
		self.__n = n
	
	def __add__(self, other):
		return Cell(self.__n + other.__n)
	
	def __sub__(self, other):
		return Cell(self.__n - other.__n)
	
	def __mul__(self, other):
		return Cell(self.__n * other.__n)
	
	def __truediv__(self, other):
		return Cell(self.__n // other.__n)
	
	def make_order(self, m):
		s = ""
		n = self.__n
		while n > 0:
			s += "*" * min(m, n) + "\n"
			n -= m
		return s

c = Cell(3) + Cell(5)
print("Cell(3) + Cell(5):", c.make_order(3), sep = "\n")

c = Cell(19) - Cell(5)
print("Cell(19) - Cell(5):", c.make_order(5), sep = "\n")

c = Cell(4) * Cell(5)
print("Cell(4) * Cell(5):", c.make_order(6), sep = "\n")

c = Cell(19) / Cell(5)
print("Cell(19) / Cell(5):", c.make_order(5), sep = "\n")
