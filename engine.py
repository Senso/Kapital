import json

from commands import Commands
from city import City

class Engine:
	def __init__(self, player, screen):
		self.player = player
		self.commands = Commands(self)
		self.screen = screen
		self.city = None
		self.menus = None
		self.current_menu = None
		
	def preload_menus(self):
		self.menus = json.load(open('data/menus.cfg'))
		
	def start(self):
		print 'Starting'
		self.update_options(self.menus['title_menu'])
		self.screen.update_main_win('Title Screen')
		self.screen.init_screen()
		
	def update_options(self, menu_data):
		# Unbind all previous keys
		if self.current_menu is not None:
			for option in self.current_menu['options'].items():
				self.screen.root.unbind(option[0])
			
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
				
		self.current_menu = menu_data
		self.screen.update_opts_win(txt)
		
	def new_game(self):
		self.city = City()
		self.city.generate_name()
		self.city.generate_districts()
		
		self.player.money = 1000000

		self.commands.show_city(None)
		self.update_options(self.menus['city_overview_menu'])
		
	def display_city_menu(self, districts=None):
		if districts is None:
			# By default, we sort by district name
			districts = self.city.districts.keys()
			districts.sort()
		lmax = max(len(w) for w in districts) + 1
		
		ntext = "City: \n%s\n\n" % self.city.name
		ntext += "%s%s%s\n" % ('District'.ljust(lmax), 'Households'.ljust(lmax), 'Median income'.ljust(lmax))
		for d in districts:
			ntext += "%s%s$%s\n" % (d.ljust(lmax), str(self.city.districts[d].households).ljust(lmax), str(self.city.districts[d].median_income).ljust(lmax))
			
		self.screen.update_main_win(ntext)
		self.update_options(self.menus['city_overview_menu'])
		
	def end_turn(self):
		self.player.end_turn()
		txt = "%s\nTurn: %s" % (self.player.date.ctime(), self.player.turn)
		self.screen.update_head_win(txt)
		
		
