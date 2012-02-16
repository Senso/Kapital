import curses

class Screen:
	def __init__(self, stdscr):
		self.screen = stdscr
		self.height = 40
		self.width = 80
		self.curx, self.cury = 0, 0
	
	def catch_key(self):
		# depending on menu, process keys and run callbacks
		while True:
			key = self.screen.getch()
			if key == 'q':
				break
	
	def title_menu(self, menu):
		# get the title menu from the config
		# display it
		self.screen.clear()
		self.screen.addstr(2, 2, menu['title'])
		offset = 3
		for option in menu['options'].items():
			o_str = option[0]
			o_key = option[1][0]
			o_callback = option[1][1]
			self.screen.addstr(offset + 1, 5, o_str)
		self.catch_key()
		
	def main_loop(self):
		# Find in which menu the player is and
		# lookup the corresponding valid keys
		self.catch_key()