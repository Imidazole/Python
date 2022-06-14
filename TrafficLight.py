import time

class TrafficLight:
	__color = ""
	
	def _print_color(self):
		print("The color is set to", self.color)
	
	def running(self):
		self.color = "green"
		self._print_color()
		time.sleep(7)
		self.color = "yellow"
		self._print_color()
		time.sleep(2)
		self.color = "red"
		self._print_color()
		time.sleep(5)

tl = TrafficLight()
tl.running()
