class Road:
	# Centimeters
	__depth = 5
	# Kilos
	__density = 25
	# Meters
	_length = 0
	# Meters
	_width = 0
	
	def __init__(self, length, width):
		self.length = length
		self.width = width
		self.depth = 5
		self.density = 25
	
	def calc_mass(self):
		return self.width * self.length * self.depth * self.density / 1000

r = Road(10000, 20)
print("{} metric tones of asphalt is needed.".format(r.calc_mass()))
