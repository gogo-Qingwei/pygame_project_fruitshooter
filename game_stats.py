from time import sleep

class GameStats():
	"""Track statitics for alien invasion."""

	def __init__(self,settings):
		self.settings = settings
		self.reset_stats()
		#if the player has no ships left, we set game_active to false
		#the game should start in an inactive state with no way for the player to start it
		#until we make a Play Button.
		#High score should never be reset.score
		self.high_score = 0
		#self.ships_left = self.settings.ship_limit

	def reset_stats(self):
		""" Initialize statisticas that can change during the game. """
		sleep(0.6)
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.blood = 100
		

 