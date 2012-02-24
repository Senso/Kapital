import json
from math import floor
from random import randint, choice, randrange, random

class City:
	def __init__(self):
		self.name = ''
		self.districts = {}
		
	def generate_name(self):
		names = json.load(open('data/cities.cfg'))
		self.pre1 = choice(names['prefix'])
		self.pre2 = choice(names['prefix'])
		self.suf = choice(names['suffix'])
		self.name = self.pre1.capitalize() + self.pre2 + self.suf
		return self.name
	
	def generate_districts(self):
		num_districts = randrange(10,20)
		while num_districts > 1:
			d = District()
			name = d.generate_name()
			d.generate_pop()
			if name not in self.districts.keys():
				self.districts[name] = d
				num_districts -= 1
				
		ds = self.districts.keys()
		
		# Determine income level, based on the following totally non-scientific
		# formula: 25% poor, 60% middle-class, 15% rich (rounded down, bias middle-class)
		poor = int(floor(float(len(ds)) * 0.25))
		middle = int(floor(float(len(ds)) * 0.60))
		rich = int(floor(float(len(ds)) * 0.15))
		middle += len(ds) - (poor + middle + rich)
	
		for dist in ds[:poor]:
			self.districts[dist].generate_income('poor')
		for dist in ds[poor:poor+middle]:
			self.districts[dist].generate_income('middle')
		for dist in ds[poor+middle:]:
			self.districts[dist].generate_income('rich')
			
	def total_pop(self):
		t_h = 0
		for d in self.districts.values():
			t_h += d.population
		return t_h
	
	def districts_info(self):
		data = []
		for d in self.districts.values():
			data.append((d.name, d.population, d.income, d.unemployed, d.unemployment_rate * 100))
		data.sort(key=lambda t: t[0])
		return data
	
	def sort_districts_by_pop(self, order='pop_asc'):
		dist = self.districts_info()
		if order == 'pop_asc':
			dist.sort(key=lambda tup: tup[1])
		else:
			dist.sort(key=lambda tup: tup[1], reverse=True)
		return dist
	
	def sort_districts_by_income(self, order='income_asc'):
		dist = self.districts_info()
		if order == 'income_asc':
			dist.sort(key=lambda tup: tup[2])
		else:
			dist.sort(key=lambda tup: tup[2], reverse=True)
		return dist

class District:
	def __init__(self):
		self.name = ''
		self.households = 0
		self.population = 0
		self.income = 0
		self.unemployed = 0
		self.unemployment_rate = 0
		#self.businesses = []

	def generate_name(self):
		names = json.load(open('data/districts.cfg'))
		self.name = choice(names['district_names'])
		return self.name
		
	def generate_pop(self):
		self.population = 60000 + randint(10000,50000) + randint(10000,100000)
		return self.population
	
	def starting_unemployment(self, level):
		base = 0.06
		if level == 'poor':
			base += random() / 4.0 + random() / 5.0
		elif level == 'rich':
			base -= random() / 4.0
		if base <= 0.0:
			base = 0.02
		self.unemployment_rate = round(base, 2)
		
		calc = float(self.population) * self.unemployment_rate
		self.unemployed = int(calc)
		
	def generate_income(self, level='middle'):
		self.starting_unemployment(level)
		
		if level == 'poor':
			#self.income = 12000 + randint(1000, 7000) + randint(1000, 6000)
			self.income = 5000 + randint(1000, 5000) + randint(4000, 10000)
		elif level == 'middle':
			#self.income = 30000 + randint(5000, 10000) + randint(2000, 7000)
			self.income = 10000 + randint(8000, 10000) + randint(2000, 20000)
		elif level == 'rich':
			self.income = 35000 + randint(3000, 20000) + randint(2000, 45000)
		return self.income
		
		