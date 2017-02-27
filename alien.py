import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, settings, screen):
		super().__init__()
		self.screen = screen
		self.settings = settings
		self.screen_rect = self.screen.get_rect()
		self.alien_img_set = []
		alien_list=[
			'assets/bomb01.png',
			'assets/bomb02.png',
			'assets/bomb03.png',
			'assets/bomb04.png',
			'assets/bomb05.png',
			'assets/bomb06.png',
			'assets/bomb07.png',
			'assets/bomb08.png',
			'assets/bomb09.png',
			'assets/bomb10.png']
		for alien in alien_list:
			self.alien_img_set.append(pygame.image.load(alien).convert_alpha())
		
		#Load the alien image and set its rect attribute.
		self.image_random = random.choice(self.alien_img_set)
		self.image =  self.image_random.copy()
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.width * 0.75 / 2)
		# Start each new alien near the top left of the screen.
		self.rect.x = random.randrange(self.rect.width, settings.screen_width - self.rect.width)
		self.rect.y = random.randrange(-100,-50)
		#random move
		self.alien_speed_x = random.randrange(-1,1)
		self.alien_speed_y = random.randrange(1,8)
		#Store the alien's exact position.
		#add rotation
		self.rotation = 5
		self.rotation_speed = random.randrange(-4,7)
		self.last_update = pygame.time.get_ticks()
		self.x = float(self.rect.x)
 
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <=0:
			return True
 
	def rotate(self):
		time = pygame.time.get_ticks()
		if time - self.last_update > 60: #milliseconds
			self.last_update = time 
			self.rotation = (self.rotation + self.rotation_speed) % 360
			self.image = pygame.transform.rotate(self.image_random, self.rotation)

	def update(self):
		"""Move the alien right"""
		self.rotate()
		self.rect.x += self.alien_speed_x
		self.rect.y += self.alien_speed_y
		if (self.rect.top > self.settings.screen_height + 40) or (self.rect.left < -35) or (self.rect.right > self.settings.screen_width + 20):
			self.rect.x = random.randrange(0, self.settings.screen_width - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(2, 7)  

	
	def blitme(self):
		#Blitting is a process of putting one image onto another
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)