import pygame
from pygame.sprite import Sprite
import random

class Bullet(Sprite):
	#when you use sprites, you can group related elements in your game
	def __init__(self, settings, screen, x, y):
		#create a bullet object at the ship's current position
		super(Bullet, self).__init__()
		self.screen = screen
		self.bullet_set = []
		bullets=[
			'assets/wood1.png',
			'assets/wood2.png']
		for i in bullets:
			self.bullet_set.append(pygame.image.load(i).convert_alpha())

		self.bullet = random.choice(self.bullet_set)
		# self.bullet = self.bullet_random.copy()
		self.rect = self.bullet.get_rect()
		self.rect.centerx = x
		self.rect.top = y

		#Store the bullet's position as a decimal value so we can make
		#fine adjustments to the bullet’s speed
		self.y = self.rect.y
		self.speed_factor = settings.bullet_speed_factor		

	def update(self):
		#manage the bullet position, move the bullets up the screen
		#update the decimal position of the bullet
		self.y -= self.speed_factor #update vertical coordinat position
		self.rect.y = self.y 

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		self.screen.blit(self.bullet, self.rect) # we loop through the sprites in the bullets and call draw_bullet() on each one. 

