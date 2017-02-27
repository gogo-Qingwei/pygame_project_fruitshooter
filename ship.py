# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:15:01 2017
"""
import pygame
from pygame.sprite import Sprite
    
class Ship(Sprite):
    def __init__(self,settings, screen, ship_img): 
        super().__init__()
        self.screen = screen    
        self.settings = settings
        self.image = ship_img
        #so we can use attributes in update()
        self.rect = self.image.get_rect()
        self.radius = 20
        self.screen_rect = screen.get_rect() #access the surface's rectangles attribute
        self.rect.centerx = self.screen_rect.centerx #we have center,centerx,centery attributes of a rect
        self.rect.bottom = self.screen_rect.bottom - 12 
        #an edge of the screen
        #the origin(0,0) is at the top-left corner of the screen

        self.last_shot = pygame.time.get_ticks()
        self.ship_left = self.settings.ship_limit
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_timer = pygame.time.get_ticks()
        self.center = float(self.rect.centerx)
        #Store a decimal value for the ship's center.
        #rect will store only the integer portion of that value.
        self.moving_right = False
        #check_events() so that moving_right is set to True when the
        #right arrow key is pressed and False when the key is released
        self.moving_left = False
    
    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (self.settings.screen_width / 2, self.settings.screen_height + 200)

    def center_ship(self):
        self.center = self.screen_rect.centerx
   
    def update(self):
        # time out for powerups
        if self.power >=3 and pygame.time.get_ticks() - self.power_time > 100:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        #update rect object from self.center.
        self.rect.centerx = self.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect) #draw the image to the screen at the position specified by self.rect
          