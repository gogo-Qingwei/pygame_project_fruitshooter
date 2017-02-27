from pygame.sprite import Sprite
import pygame
import random

class Power(Sprite):
	def __init__(self, settings, center, screen):
		super().__init__()	
		self.settings = settings
		self.image = pygame.image.load('assets/lightning.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.y = float(self.rect.y)
		self.screen = screen
		self.power_speed_factor = 3

	def update(self):
		self.y += self.power_speed_factor
		self.rect.y = self.y
		if self.rect.bottom < 0:
			self.kill()

	def draw_powerup(self):
 		self.screen.blit(self.image, self.rect)


