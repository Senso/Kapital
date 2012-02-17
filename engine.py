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
		
	def show_menu(self, menu):
		self.player.current_menu = menu
		self.screen.display_menu(self.menus[menu])
		
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
		self.show_menu('title_menu')
		self.main_loop()
		#callback = self.screen.display_menu(self.menus['title_menu'])
		#self.process_callback(callback)
		
	def quit(self):
		sys.exit(0)
		
	def main_loop(self):
		while True:
			key = self.screen.catch_key(self.menus[player.current_menu]['options'])
			self.process_callback(key)
		
	def new_game(self):
		# generate City name
		# generate districts
		# initialize player
		# show main city view menu and start main loop
		self.city = City()
		self.city.generate_name()
		self.log('city name: ' + self.city.name)
		self.city.generate_districts()
		for d in self.city.districts.values():
			self.log("%s: %s" % (d.name, str(d.households) + ', ' + str(d.median_income)))
			
		self.show_menu('city_overview_menu')
		#self.main_loop()
