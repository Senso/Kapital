import json
from random import randint, choice, randrange

class City:
	def __init__(self):
		self.name = ''
		self.districts = {}
		
	def generate_name(self):
		pass
	
	def generate_districts(self):
		tmp_d = randrange(10,20)
		while tmp_d > 1:
			d = District()
			
			name = d.generate_name()
			if name not in self.districts.keys():
				self.districts[name] = d
				tmp_d -= 1
	

class District:
	def __init__(self):
		self.name = ''
		self.households = 0
		self.median_income = 0
		
	def generate_name(self):
		names = json.load(open('data/districts.cfg'))
		self.name = choice(names)
		return self.name
		
	def generate_households(self):
		self.households = 25000 + randint(2000, 10000) + randint(2000,15000)
		return self.households
		
	def generate_income(self, level='middle'):
		if level == 'poor':
			self.median_income = 12000 + randint(1000, 7000) + randint(1000, 6000)
		elif level == 'middle':
			self.median_income = 30000 + randint(5000, 10000) + randint(2000, 7000)
		elif level == 'rich':
			self.median_income = 60000 + randint(5000, 10000) + randint(10000, 40000)
		return self.median_income
		
		