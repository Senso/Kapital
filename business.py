from random import randrange, choice

class Business:
	def __init__(self, game):
		self.game = game
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
		self.money = 150000 + randrange(5000,50000) + randrange(1000,10000)
		
	def randomize_production(self, ind, res):
		industry = choice(ind.keys())
		self.prod_data = {industry: ind[industry]}
		self.producing = self.prod_data[industry]['produces'][0]
		self.resource_data = res[self.producing]
		
	def hire_employees(self):
		d = self.game.city.districts[self.district]
		biz = self.prod_data.values[0]
		needed = biz['max_employees'] - self.employees
		if d.unemployed - needed >= 0:
			d.unemployed -= needed
			self.employees += needed
		else:
			will_hire = needed - d.unemployed
			d.unemployed -= will_hire
			self.employees += will_hire
		
	def end_turn(self):
		pass
		
		
	
	