import json
from string import Template

from commands import Commands
from city import City

class Engine:
	def __init__(self, player, screen):
		self.player = player
		self.commands = Commands(self)
		self.screen = screen
		self.city = None
		self.menus = None
		
	def preload_menus(self):
		self.menus = json.load(open('data/menus.cfg'))
		
	def start(self):
		print 'Starting'
		self.update_options(self.menus['title_menu'])
		self.display_main_menu()
		self.screen.init_screen()
		
	def update_options(self, menu_data):
		txt = ''
		for option in menu_data['options'].items():
			o_key = option[0]
			o_str = option[1][0]
			o_cb  = option[1][1]
			txt += "(%s) %s\n" % (o_key, o_str)
			
			# Bind callbacks
			cmd = getattr(self.commands, o_cb)
			if cmd:
				self.screen.root.bind(o_key, func=cmd)
		self.screen.update_opts_win(txt)
	
	def display_main_menu(self):
		self.screen.update_main_win('Welcome to huh...')
		
	def display_city_menu(self):
		lmax = max(len(w) for w in self.city.districts.keys()) + 1
		print 'lmax', lmax
		
		ntext = "City: \n%s\n\n" % self.city.name
		ntext += "%s%s%s\n" % ('District'.ljust(lmax), 'Households'.ljust(lmax), 'Median income'.ljust(lmax))
		for d in self.city.districts.values():
			ntext += "%s%s$%s\n" % (d.name.ljust(lmax), str(d.households).ljust(lmax), str(d.median_income).ljust(lmax))
		self.screen.update_main_win(ntext)
		
	def new_game(self):
		self.city = City()
		self.city.generate_name()
		self.city.generate_districts()

		self.commands.show_city(None)
		self.update_options(self.menus['city_overview_menu'])
