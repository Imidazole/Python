class ComplexNumber:
	__r = 0
	__i = 0
	
	def __init__(self, r, i):
		self.__r = r
		self.__i = i
	
	def __add__(self, other):
		r = self.__r + other.__r
		i = self.__i + other.__i
		return ComplexNumber(r, i)
	
	def __mul__(self, other):
		r = self.__r * other.__r - self.__i * other.__i
		i = self.__r * other.__i + self.__i * other.__r
		return ComplexNumber(r, i)
	
	def __str__(self):
		return f"{self.__r} + i * {self.__i}"

c1 = ComplexNumber(1, 0)
c2 = ComplexNumber(5, 6)

print("(", c1, ") * (", c2, ") =", c1 * c2)

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(-5, 4)

print("(", c1, ") * (", c2, ") =", c1 * c2)
