import json

class Engine:
	def __index__(self):
		self.menus = None
		
	def load_menus(self):
		self.menus = json.load(open('data/menus.cfg'))
		