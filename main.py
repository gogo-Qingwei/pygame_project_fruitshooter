import sys
# use the sys module to exist the game
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien 
from game_stats import GameStats
from scoreboard import Scoreboard
import Frontpage

def run_game(): 
    pygame.init()
    pygame.mixer.init()#music
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height)) #define screen size, represent the entire game window 
    pygame.display.set_caption("Shot Fruit!")
    clock = pygame.time.Clock() 
    #imgs======================================================
    ship_img = pygame.transform.scale(pygame.image.load('assets/player.png').convert_alpha(), (54,54))
    ship_img.set_colorkey(ship_img.get_at((0,0)))
    #============================================================
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    #make a group to store bullets in.This group is created outside of the while loop so we
    #don’t create a new group of bullets 34 each time the loop cycles.
    ship = Ship(settings, screen, ship_img) #make an instance of ship
    bullets = Group()#create an empty group called aliens 
    aliens = Group()#create the fleet of alplayer_img = pygame.image.load('assets/player.png').convert()  
    expls = Group()  
    for i in range(8):    
        gf.create_alien(settings, screen, aliens)
    powerups = Group()
    #================================================================================
    running = True
    menu = True
    while running:
        if menu:
            Frontpage.title_page(screen, settings)
            pygame.time.wait(1000) 
            pygame.mixer.music.load("sounds/background.ogg")#start game music
            pygame.mixer.music.play(-1) #make the music in an endless loop
            menu = False

        clock.tick(settings.FPS)  
        gf.check_events(settings, screen, stats, sb, ship, aliens, 
                           bullets)  
   
        ship.update() 
        gf.update_bullets(settings, screen, stats, sb, ship, aliens, powerups, bullets)
        gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets, powerups)
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, powerups)
    #================================================================================

run_game()   