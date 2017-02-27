# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:44:01 2017
"""
# initialize attributes controlling the game's appearance and the ship's speed
import pygame
from scoreboard import Scoreboard


class Settings():
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 560
        self.FPS = 60 #Frames Per Second
        self.bar_width = 155
        self.bar_height = 14

        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 255,0)
        self.text_color = (255,0,255)

        self.bg_color = (230,230,230)
        self.ship_speed_factor = 5
        #the number of ships the player starts with.
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 4
        self.bullet_height = 25
        self.bullet_color = 255,255,255
        self.bullets_allowed = 8
        #alien settings
        #how quickly the alien point values increase
        self.score_scale = 1.5
 
    #make the game more challenging by increasing the speed of the game each time a player clears
    #the screen
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1
        # Scoring.
        self.alien_points = 50
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale 
        self.alien_points = int(self.alien_points * self.score_scale)

