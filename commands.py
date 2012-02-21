import sys

class Commands:
	def __init__(self, engine):
		self.game = engine
	
	def quit(self, screen):
		sys.exit(0)
		
	def end_turn(self, screen):
		self.game.end_turn()
	
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
		text += "Cash: $%s\n"  % self.game.player.money
		
		self.game.screen.update_main_win(text)
		
	def sort_households(self, screen):
		if self.game.player.order_mode == 'households_desc':
			self.game.player.order_mode = 'households_asc'
		elif self.game.player.order_mode == 'households_asc':
			self.game.player.order_mode = 'households_desc'
		else:
			self.game.player.order_mode = 'households_asc'
			
		s = self.game.city.sort_districts_by_households(self.game.player.order_mode)
		self.game.display_city_menu(s)
	
	def sort_income(self, screen):
		if self.game.player.order_mode == 'income_desc':
			self.game.player.order_mode = 'income_asc'
		elif self.game.player.order_mode == 'income_asc':
			self.game.player.order_mode = 'income_desc'
		else:
			self.game.player.order_mode = 'income_asc'
			
		s = self.game.city.sort_districts_by_income(self.game.player.order_mode)
		self.game.display_city_menu(s)
		