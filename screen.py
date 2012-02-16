
class Screen:
	def __init__(self, stdscr):
		self.screen = stdscr
		self.height = 40
		self.width = 80
		self.curx, self.cury = 0, 0
	
	def catch_key(self, opts):
		# depending on menu, process keys and run callbacks
		keys = opts.keys()
		while True:
			key = self.screen.getch()
			if key in keys:
				return keys[key][1]
				
	def display_menu(self, menu):
		# get the title menu from the config
		# display it
		self.screen.clear()
		self.screen.addstr(2, 2, menu['title'])
		offset = 3
		for option in menu['options'].items():
			o_key = option[0]
			o_str = option[1][0]
			self.screen.addstr(offset + 1, 5, "(%s) %s" % (o_key, o_str))
			offset += 1
		callback = self.catch_key(menu['options'])
		return callback
		
	def main_loop(self):
		# Find in which menu the player is and
		# lookup the corresponding valid keys
		self.catch_key()