#import curses
#from screen import Screen
from engine import Engine
from player import Player

if __name__ == '__main__':
	game = Engine(Player())
	game.preload_menus()
	
	game.start()
