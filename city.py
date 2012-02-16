import json
import random

class City:
	def __init__(self):
		self.name = ''
		self.districts = {}
		
	def generate_name(self):
		pass
	
	def generate_districts(self):
		tmp_d = random.randrange(10,20)
		while tmp_d > 1:
			d = District()
			name = d.generate_name()
			if name not in self.districts.keys():
				self.districts[name] = d
				tmp_d -= 1
	

class District:
	def __init__(self):
		self.name = ''
		self.population = 0
		self.crime_rate = 0.0
		self.median_income = 0
		self.poverty_level = 0.0
		
	def generate_name(self):
		names = json.load(open('data/districts.cfg'))
		return random.choice(names)
		
		