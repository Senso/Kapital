from random import randrange, choice

class Business:
	def __init__(self):
		self.money = 0
		self.name = ''
		self.suppliers = {}
		self.producing = None
		self.district = None
		self.stocks = {}

	def generate_name(self):
		# Placeholder
		self.name = 'Company ' + str(randrange(1,1000))
		
	def starting_funds(self):
		self.money = 50000 + randrange(5000,50000) + randrange(1000,10000)
		
	def randomize_production(self, res):
		category = choice(res.keys())
		industry = choice(res[category])
		self.producing = industry
		
	def end_turn(self):
		pass
		
		
	
	