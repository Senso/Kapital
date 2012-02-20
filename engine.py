import json
from string import Template

from commands import Commands
from city import City
from tk_win import Tk_win

class Engine:
	def __init__(self, player):
		self.player = player
		self.commands = Commands(self)
		self.screen = Tk_win(self.commands)
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
				
				if len(i[1]) == 2 and i[1][1] == 'multiline':
					tpl_data[i[0]] = self.format_multiline(tpl_data[i[0]])
		else:
			tpl_data = {}
				
		end_result = {'data': tpl_data, 'options': self.menus[menu]['options'], 'title': self.menus[menu]['title']}

		self.player.current_menu = menu
		return end_result
		
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
		print 'Starting'
		self.screen.init_screen(self.show_menu('title_menu'))
		
	def format_multiline(self, data):
		print type(data)
		formatted = '\n'
		for i in data:
			#print i
			formatted += "\t".join(i)
			#formatted += '\n'
		return formatted
		
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
			'districts_info': self.city.districts_info()
		}
		self.screen.update_menu(self.show_menu('city_overview_menu', data))
