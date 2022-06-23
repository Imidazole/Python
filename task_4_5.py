from abc import ABC, abstractmethod

class Warehouse:
	d = dict()	
	
	def place_item(self, item, quantity):
		if not isinstance(quantity, int):
			return None
		if item not in d.keys():
			d[item] = 0
		d[item] += quantity

class OfficeTechnique:
	vendor = ""
	year_of_purchasing = 2000
	size = 0
	weight = 0
	
	def __item__(self, vendor, year_of_purchasing, size, weight):
		self.vendor = vendor
		self.year_of_purchasing = year_of_purchasing
		self.size = size
		self.weight = weight

class Printer(OfficeTechnique):
	is_compact = True
	def __init__(self, is_compact, *args):
		super().__init__(self, *args)
		self.is_compact = is_compact

class Scanner(OfficeTechnique):
	def __init__(self, *args):
		super().__init__(self, *args)

class Copier(OfficeTechnique):
	printing_capacity = False
	scanning_capacity = False
	def __init__(self, *args):
		super().__init__(self, *args)
