import sys
import json

from city import City

class Engine:
	def __init__(self, player, screen):
		self.player = player
		self.screen = screen
		self.city = None
		self.menus = None
		
	def preload_menus(self):
		self.menus = json.load(open('data/menus.cfg'))
		
	def process_callback(self, cb):
		self.log('callback: ' + cb)
		cmd = getattr(self, cb)
		if cmd:
			cmd()
			
	def log(self, str):
		f = open('cap.log', 'a')
		f.write(str + '\n')
		f.close()
		
	def start(self):
		self.screen.set_borders()
		
		callback = self.screen.display_menu(self.menus['title_menu'])
		self.process_callback(callback)
		
	def quit(self):
		sys.exit(0)
		
	def new_game(self):
		# generate City name
		# generate districts
		# initialize player
		# show main city view menu and start main loop
		self.city = City()
		self.city.generate_name()
		self.log('city name: ' + self.city.name)
		self.city.generate_districts()
		self.log('districts: ' + str(self.city.districts))
