from random import randrange, choice

class Business:
	def __init__(self, data):
		self.money = 0
		self.name = ''
		self.suppliers = {}
		self.producing = None
		self.prod_data = None
		self.resource_data = None
		self.district = None
		self.stocks = {}
		self.employees = 0

	def generate_name(self):
		self.name = self.prod_data.keys()[0].capitalize() + ' #' + str(randrange(1,1000))
		
	def starting_funds(self):
		self.money = 50000 + randrange(5000,50000) + randrange(1000,10000)
		
	def randomize_production(self, ind, res):
		industry = choice(ind.keys())
		self.prod_data = {industry: ind[industry]}
		self.resource_data = res[self.prod_data[produces]]
		
	def end_turn(self):
		pass
		
		
	
	