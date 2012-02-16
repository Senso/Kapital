
from screen import Screen
from engine import Engine

def main():
	screen = Screen()
	screen.title_menu(game.menus['title_menu'])
	

if __name__ == '__main__':
	# Load config and all menus in memory
	game = Engine()
	game.load_menus()

	curses.wrapper(main)
