import json

class Engine:
	def __init__(self, player, screen):
		self.player = player
		self.screen = screen
		self.menus = None
		
	def preload_menus(self):
		self.menus = json.load(open('data/menus.cfg'))
		
	def process_callback(self, cb):
		cmd = getattr(self, cb)
		if cmd:
			cmd()
			
	def log(self, str):
		f = open('cap.log', 'wa')
		f.write(str + '\n')
		f.close()
		
	def start(self):
		self.screen.set_borders()
		
		callback = self.screen.display_menu(self.menus['title_menu'])
		self.log('callback ' + callback)
		
	def quit(self):
		import sys
		sys.exit(0)
		
	def new_game(self):
		# generate City name
		# generate districts
		# initialize player
		# show main city view menu and start main loop
		print 'new_game placeholder'
