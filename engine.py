import json

class Engine:
	def __index__(self):
		self.menus = None
		
	def load_menus(self):
		json_data = json.load(open('data/menus.cfg'))
		self.menus = json_data['menus']
		