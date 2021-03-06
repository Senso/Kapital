from curses import newwin, ascii

class Screen:
	def __init__(self, stdscr):
		self.screen = stdscr
		self.height = 30
		self.width = 80
		self.curx, self.cury = 0, 0
		#self.screen.resize(self.height, self.width)
		
		self.dat_scr = newwin(20, 80, 0, 0)
		self.opt_scr = newwin(10, 80, 20, 0)
		
		self.dat_scr.refresh()
		self.opt_scr.refresh()
		self.screen.refresh()
	
	def catch_key(self, opts):
		# depending on menu, process keys and run callbacks
		while True:
			key = self.screen.getkey()
			if key in opts.keys():
				return opts[key][1]
				
	def set_borders(self):
		self.dat_scr.box()
		self.opt_scr.box()
				
	def display_menu(self, menu):
		# get the title menu from the config
		# display it
		#self.screen.clear()
		self.dat_scr.clear()
		self.opt_scr.clear()
		
		self.set_borders()
		self.dat_scr.addstr(2, 2, menu['title'])
		
		if menu['data'].items():
			for d in menu['data'].items():
				label = d[0]
				val = d[1]
				self.dat_scr.addstr(ascii.LF + ascii.CR + "%s: %s" % (label, val))
				offset += 1
			self.dat_scr.refresh()
		
		
		for option in menu['options'].items():
			o_key = option[0]
			o_str = option[1][0]
			self.opt_scr.addstr("(%s) %s" % (o_key, o_str) + ascii.LF + ascii.CR)
			
		self.opt_scr.refresh()
		
		#callback = self.catch_key(menu['options'])
		#return callback
		
	def main_loop(self):
		# Find in which menu the player is and
		# lookup the corresponding valid keys
		self.catch_key()