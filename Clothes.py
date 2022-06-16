from abc import abstractmethod, ABC

class Clothes:
	@abstractmethod
	def tissue_spending(self):
		pass

class Coat(Clothes):
	__V = 0
	
	def __init__(self, V):
		self.__V = V
	
	@property
	def V(self):
		return self.__V
	
	@V.setter
	def V(self, new):
		self.__V = new
	
	def tissue_spending(self):
		return self.__V / 6.5 + 0.5
	
class Suit(Clothes):
	__H = 0
	
	def __init__(self, H):
		self.__H = H
	
	@property
	def H(self):
		return self.__H
	
	@H.setter
	def H(self, new):
		self.__H = new
	
	def tissue_spending(self):
		return self.__H * 2 + 0.3

c = Coat(42)
print("Размер пальто:", c.V, sep = "\n")
c.V = 45
print("Размер пальто после изменения:", c.V, sep = "\n")
print("Расход ткани:", c.tissue_spending(), sep = "\n")

s = Suit(170)
print("Размер костюма:", s.H, sep = "\n")
s.H = 175
print("Размер костюма после изменения:", s.H, sep = "\n")
print("Расход ткани:", s.tissue_spending(), sep = "\n")
