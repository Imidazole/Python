class Matrix:
	__a = []
	
	__n = 0
	__m = 0
	
	def __init__(self, l):
		self.__a = l
		
		self.__n = len(l)
		if len(l) > 0:
			self.__m = len(l[0])
	
	def __str__(self):
		s = ""
		for i in range(self.__n):
			for j in range(self.__m):
				s += str(self.__a[i][j]) + "\t"
			s += "\n"
		return s
	
	def __add__(self, other):
		a = [[self.__a[i][j] + other.__a[i][j] 
			for j in range(self.__m)]
				for i in range(self.__n)]
		return Matrix(a)

a = [[1, 6], [7, 5], [8, 4]]
am = Matrix(a)
print("a:", am, sep = "\n")

b = [[9, 6], [0, 5], [4, 5]]
bm = Matrix(b)
print("b:", bm, sep = "\n")

cm = am + bm
print("a + b:", cm, sep = "\n")
