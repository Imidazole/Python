class Worker:
	name = ""
	surname = ""
	_income = dict()
	
	def __init__(self, name, surname, wage, bonus):
		self.name = name
		self.surname = surname
		self._income["wage"] = wage
		self._income["bonus"] = bonus

class Position(Worker):
	def get_full_name(self):
		return "{0} {1}".format(self.name, self.surname)
	
	def get_total_income(self):
		return self._income["wage"] + self._income["bonus"]

p1 = Position("John", "Malcohlm", 10000, 3000)
fn1 = p1.get_full_name()
ti1 = p1.get_total_income()

p2 = Position("Marcus", "Heinz", 5000, 1000)
fn2 = p2.get_full_name()
ti2 = p2.get_total_income()

f_string = "Full name: {0}\nTotal income: {1}"

print(f_string.format(fn1, ti1))
print(f_string.format(fn2, ti2))
