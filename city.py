import json
from math import floor
from random import randint, choice, randrange

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
			d.generate_households()
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
			
	def total_households(self):
		t_h = 0
		for d in self.districts.values():
			t_h += d.households
		return t_h
	
	def districts_info(self):
		data = []
		for d in self.districts.values():
			data.append((d.name, d.households, d.median_income))
		return data
	
	def sort_districts_by_households(self, order='households_asc'):
		new = []
		for i in self.districts.values():
			new.append((i.name, i.households, i.median_income))
		if order == 'households_asc':
			new.sort(key=lambda tup: tup[1])
		else:
			new.sort(key=lambda tup: tup[1], reverse=True)
		derp = [x[0] for x in new]
		return derp
	
	def sort_districts_by_income(self, order='income_asc'):
		new = []
		for i in self.districts.values():
			new.append((i.name, i.households, i.median_income))
		if order == 'income_asc':
			new.sort(key=lambda tup: tup[2])
		else:
			new.sort(key=lambda tup: tup[2], reverse=True)
		derp = [x[0] for x in new]
		return derp

class District:
	def __init__(self):
		self.name = ''
		self.households = 0
		self.median_income = 0
		self.unemployed = 0

	def generate_name(self):
		names = json.load(open('data/districts.cfg'))
		self.name = choice(names['district_names'])
		return self.name
		
	def generate_households(self):
		self.households = 25000 + randint(2000, 10000) + randint(2000,15000)
		return self.households
	
	def log(self, str):
		f = open('cap.log', 'a')
		f.write(str + '\n')
		f.close()
		
	def generate_income(self, level='middle'):
		if level == 'poor':
			self.median_income = 12000 + randint(1000, 7000) + randint(1000, 6000)
		elif level == 'middle':
			self.median_income = 30000 + randint(5000, 10000) + randint(2000, 7000)
		elif level == 'rich':
			self.median_income = 60000 + randint(5000, 10000) + randint(10000, 40000)
		self.log("%s: (%s) %s" % (self.name, level, self.median_income))
		return self.median_income
		
		