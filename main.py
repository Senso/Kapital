from engine import Engine
from player import Player
from tk_win import Tk_win

if __name__ == '__main__':
	game = Engine(Player(), Tk_win())
	game.preload_menus()
	
	game.start()
