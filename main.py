import curses

from engine import Engine

class Screen:
	def __init__(self, stdscr):
		self.screen = stdscr
		self.height = 40
		self.width = 80
		self.curx, self.cury = 0, 0
	
	def catch_key(self, menu_keys):
		while True:
			key = self.screen.getch()
			# depending on menu, process keys and run callbacks
	
	def title_menu(self):
		# get the title menu from the config
		# display it
		self.catch_key()
		
	def main_loop(self):
		# Find in which menu the player is and
		# lookup the corresponding valid keys
		self.catch_key()


def main(stdscr):
	screen = Screen(stdscr)
	screen.title_menu()
	


if __name__ == '__main__':
	# Load config and all menus in memory
	game = Engine()
	
	
	curses.wrapper(main)