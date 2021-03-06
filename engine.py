import json
from random import randrange, choice

from commands import Commands
from city import City
from business import Business

class Engine:
	def __init__(self, player, screen):
		self.player = player
		self.commands = Commands(self)
		self.screen = screen
		self.city = None
		self.menus = None
		self.current_menu = None
		self.resources = None
		self.industries = None
		self.ai_companies = []
		
	def preload_cfg(self):
		self.menus = json.load(open('data/menus.cfg'))
		self.resources = json.load(open('data/resources.cfg'))
		self.industries = json.load(open('data/industries.cfg'))
		
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
		# Create new city
		self.city = City()
		self.city.generate_name()
		self.city.generate_districts()
		
		# Generate AI companies
		for i in xrange(0, randrange(10, 20)):
			b = Business(self)
			b.starting_funds()
			b.randomize_production(self.industries, self.resources)
			b.generate_name()
			b.district = choice(self.city.districts.keys())
			#self.city.districts[b.district].companies.append(b)
			self.ai_companies.append(b)
		
		#for i in self.ai_companies:
		#	print i.name, i.money, i.producing, i.district
			
		self.player.money = 1000000

		self.commands.show_city(None)
		self.update_options(self.menus['city_overview_menu'])
		
	def display_city_menu(self, districts=None):
		if districts is None:
			# By default, we sort by district name
			districts = self.city.districts_info()
			
		self.screen.display_column_data("City: \n%s\n\n" % self.city.name,
			['District', 'Pop', 'Income', 'Unemployed', '%'],
			districts)

		self.update_options(self.menus['city_overview_menu'])
		
	def display_biz_menu(self, district=None):
		self.ai_companies
		self.screen.display_column_data("%s City\n\n" % self.city.name,
			['Business', 'Cash', '']
			)
		
		
	def end_turn(self):
		self.player.end_turn()
		txt = "%s\nTurn: %s" % (self.player.date.ctime(), self.player.turn)
		self.screen.update_head_win(txt)
		
		
