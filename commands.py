import sys

class Commands:
	def __init__(self, engine):
		self.game = engine
	
	def quit(self, screen):
		sys.exit(0)
	
	def new_game(self, screen):
		self.game.new_game()
		
	def show_credits(self, screen):
		pass
	
	def load_game(self, screen):
		pass
	
	def show_main_menu(self, screen):
		self.game.display_main_menu()
		
	def show_city(self, screen):
		self.game.display_city_menu()
		
	def show_corporation(self, screen):
		self.game.update_options(self.game.menus['corp_overview_menu'])
		
		text = "Name: %s\n" % self.game.player.corp_name
		text += "Cash: %s\n"  % self.game.player.money