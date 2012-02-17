import sys
import json
from string import Template

from city import City

class Engine:
	def __init__(self, player, screen):
		self.player = player
		self.screen = screen
		self.city = None
		self.menus = None
		
	def preload_menus(self):
		self.menus = json.load(open('data/menus.cfg'))
		
	def show_menu(self, menu, data={}):
		# ("Districts", ["{districts_info}", "multiline"])
		if self.menus[menu]['data']:
			tpl_data = self.menus[menu]['data']
			
			for i in tpl_data.items():
				b = Template(i[1][0])
				tpl_data[i[0]] = b.substitute(data)
		else:
			tpl_data = {}
				
		end_result = {'data': tpl_data, 'options': self.menus[menu]['options'], 'title': self.menus[menu]['title']}

		self.player.current_menu = menu
		self.screen.display_menu(end_result)
		
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
		
	def quit(self):
		sys.exit(0)
		
	def main_loop(self):
		while True:
			key = self.screen.catch_key(self.menus[self.player.current_menu]['options'])
			self.process_callback(key)
		
	def new_game(self):
		self.city = City()
		self.city.generate_name()
		self.log('city name: ' + self.city.name)
		self.city.generate_districts()
		for d in self.city.districts.values():
			self.log("%s: %s" % (d.name, str(d.households) + ', ' + str(d.median_income)))
		
		data = {
			'city_name': self.city.name,
			'total_households': self.city.total_households(),
			'districts_info': ", ".join(self.city.districts.keys())
		}
		self.show_menu('city_overview_menu', data)
