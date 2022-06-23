class Date:
	__day = 1
	__month = 1
	__year = 2000
	
	def __init__(self, day, month, year):
		self.__day = day
		self.__month = month
		self.__year = year
	
	@classmethod
	def parse_date_string(cls, date_string):
		ar = date_string.split("-")
		if len(ar) == 3:
			return int(ar[0]), int(ar[1]), int(ar[2])
	
	@classmethod
	def get_date_by_string(cls, date_string):
		day, month, year = cls.parse_date_string(date_string)
		if cls.is_valid(day, month, year):
			return cls(day, month, year)
	
	@staticmethod
	def is_valid(day, month, year):
		is_year_valid = (year > 0)
		is_month_valid = (month >= 1) and (month <= 12)
		is_day_valid = ((month in {1, 3, 5, 7, 8, 10, 12}) and (day <= 31)) or\
				((month in {4, 6, 9, 11}) and (day <= 30)) or\
				((month == 2) and (day <= 28 + (year % 4 == 0) -\
								(year % 100 == 0) +\
								(year % 400 == 0))) and\
				day >= 1
		return is_year_valid and is_month_valid and is_day_valid
	
	@property
	def day(self):
		return self.__day
	
	@property
	def month(self):
		return self.__month
	
	@property
	def year(self):
		return self.__year

def check_none(date):
	if date:
		return f"Day: {date.day} Month: {date.month} Year: {date.year}"
	else:
		return "Invalid format"

sl = ["12-05-2009", "29-02-1992", "29-02-1993", "29-02-2000", "31-06-2000", "30-13-2000"]
for s in sl:
	print("String:", s)
	d = Date.get_date_by_string(s)
	print(check_none(d))
