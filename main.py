import curses
from screen import Screen
from engine import Engine
from player import Player

def main(stdscr):
	# main game initialization
	game = Engine(Player(), Screen(stdscr))
	game.preload_menus()
	game.start()
	

if __name__ == '__main__':
	curses.wrapper(main)
