class Car:
	speed = 0
	color = ""
	name = ""
	is_police = False
	
	def go(self):
		print(f"{self.name} go!")
		
	def stop(self):
		print(f"{self.name} stopped!")
	
	def turn(self, direction):
		print(f"{self.name} turned {direction}")
	
	def show_speed(self):
		pass

class TownCar(Car):
	def show_speed(self):
		if self.speed > 60:
			print(f"Speed of the {self.name} is too high ({self.speed})!")

class SportCar(Car):
	pass
	
class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40:
			print(f"Speed of the {self.name} is too high ({self.speed})!")

class PoliceCar(Car):
	def __init__(self):
		self.is_police = True

tc = TownCar()
tc.name = "TownCar"
tc.speed = 70
tc.go()
tc.turn("left")
tc.show_speed()
tc.stop()

sc = SportCar()
sc.name = "SportCar"
sc.speed = 34
sc.go()
sc.turn("right")
sc.show_speed()
sc.stop()

pc = PoliceCar()
pc.name = "PoliceCar"
pc.speed = 50
pc.go()
pc.turn("right")
print(pc.is_police)
pc.stop()

wc = WorkCar()
wc.name = "WorkCar"
wc.speed = 45
wc.go()
wc.show_speed()
wc.stop()
