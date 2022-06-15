class Stationery:
	title = ""
	
	def draw(self):
		print("Запуск отрисовки.")

class Pen(Stationery):
	def __init__(self):
		self.title = "Pen"
	
	def draw(self):
		print("This is a pen.")

class Pencil(Stationery):
	def __init__(self):
		self.title = "Pencil"
	
	def draw(self):
		print("This is a pencil.")

class Handle(Stationery):
	def __init__(self):
		self.title = "Handle"
	
	def draw(self):
		print("This is a handle.")

s = Stationery()
s.draw()

p = Pen()
p.draw()

p = Pencil()
p.draw()

h = Handle()
h.draw()
