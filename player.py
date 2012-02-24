from datetime import date, timedelta

class Player:
	def __init__(self):
		self.current_menu = None
		self.money = None
		self.corp_name = 'PlayerCorp'
		self.date = date(1990, 1, 1)
		self.turn = 1
		
		self.order_mode = ''
		
	def end_turn(self):
		self.turn += 1
		self.date = self.date + timedelta(weeks=1)
		