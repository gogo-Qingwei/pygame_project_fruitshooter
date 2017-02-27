# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:01:17 2017
"""
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from os import path
import Frontpage
import random
from powerup import Power
from time import sleep
from scoreboard import Scoreboard

#===========================================================================
def check_events(settings, screen, stats, sb, ship, 
                aliens, bullets):  
    for event in pygame.event.get(): #event is an action that the users performs=press a key or move the mouse 
        if event.type == pygame.QUIT:
            sys.exit()  #Use pygame.KEYDOWN and pygame.KEYUP to detect if a key is physically
                        #pressed down or released.   
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,settings, screen, ship)

def check_keydown_events(event, settings, screen, ship, bullets): #EACH KEYPREE IS REGISTED AS A KEYDOWN EVENT
    if event.key == pygame.K_RIGHT:#MOVE THE SHIP TO THE RIGHT. iF THE RIGHT ARROW KEY WAS PRESSED, WE MOVE THE
    #SHIP TO THE RIGHT BY INCREASING THE VALUE BY 1
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_SPACE:  
        fire_bullet(settings, screen, ship, bullets)#create a new bullet and add it to the bullets group.
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event,ai_settings, screen, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

# def Initialize_game(settings, screen, stats, sb, ship,
#         aliens, bullets): 
#         settings.initialize_dynamic_settings()
#         #Hide the mouse cursor.
#         pygame.mouse.set_visible(False)
#         #reset the game stats, high score remains no change.
#         stats.reset_stats() #reset the scoreboard images
#         sb.prep_score()
#         sb.prep_high_score()
#         sb.prep_ships() #empty the list of aliens and bullets
#         aliens.empty()
#         bullets.empty()#create a new fleet and center the ship
#         ship.center_ship()
        
# def figure_hit(screen, x, y, figures, img, stats, sb):
#     if stats.figure_left > 0:
#         stats.figure_left -= 1
#         sb.prep_ships()
#     else:
#         pygame.mouse.set_visible(True)
#
#bullets part
def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    if len(bullets) < settings.bullets_allowed: #create a new bullet and add it to the bullets group.bullets
        new_bullet = Bullet(settings, screen, ship.rect.centerx, ship.rect.top)
        bullets.add(new_bullet)# stores the new bullet in the group bullets.

    now = pygame.time.get_ticks()
    if now - ship.last_shot > 150:
        ship.last_shot = now
        if ship.power == 1:
            bullet = Bullet(settings, screen, ship.rect.centerx, ship.rect.top)
            bullets.add(bullet)
        if ship.power == 2:
            bullet1 = Bullet(settings, screen, ship.rect.left, ship.rect.centery)
            bullet2 = Bullet(settings, screen, ship.rect.right, ship.rect.centery)
            bullets.add(bullet1)
            bullets.add(bullet2)
        if ship.power >=3:
            bullet1 = Bullet(settings, screen, ship.rect.left, ship.rect.centery)
            bullet2 = Bullet(settings, screen, ship.rect.right, ship.rect.centery)
            bullet3 = Bullet(settings, screen, ship.rect.centerx, ship.rect.top)
            bullets.add(bullet1)
            bullets.add(bullet2)
            bullets.add(bullet3)

#updatedfs bullets===============================================================
def update_bullets(settings, screen, stats, sb, ship, aliens, powerups, bullets):
    bullets.update()
    random_sounds = []
    for sound in ['sounds/woosh.wav','sounds/woosh1.wav','sounds/woosh2.wav']:
        random_sounds.append(pygame.mixer.Sound(sound))
    pygame.mixer.music.set_volume(0.3) 
    #get rid of bullets that have disappeard.
    #shouldn't remvoe items from a list or group within a for loop
    #we can remove a copy of the group.
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
            
    #check for any bullets that have hit aliens.     
    check_bullet_alien_collisions(settings, screen, stats, sb, ship,
        aliens, bullets, powerups, random_sounds)
    check_high_score(stats, sb)

# THE COLLISIONS BETWEEN bullets and aliens
def check_bullet_alien_collisions(settings, screen, stats, sb, ship,
        aliens, bullets, powerups, random_sounds):
    """Respond to bullet-alien collisions."""
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)#Remove any bullets and aliens that have collided.
    for col in collisions:
        stats.score += 50
        sb.prep_score()
        random.choice(random_sounds).play()
        if random.random() > 0.92:
            power = Power(settings, col.rect.center, screen)
            powerups.add(power)
        create_alien(settings, screen, aliens)

def create_alien(settings, screen, aliens):
    """Create a full fleet of aliens"""
    alien = Alien(settings, screen)
    aliens.add(alien)

def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

#update_aliens===============================================================
def update_aliens(settings, screen, stats, sb, ship, aliens, bullets, powerups):
    """
    Check if the fleet is at an edge, then update the postions of all aliens in the fleet.
    """
    aliens.update()
    powerups.update()
    # Look for alien-ship collisions.

    collisions = pygame.sprite.spritecollide(ship, aliens, True, pygame.sprite.collide_circle)
    for col in collisions:
        sb.blood -= col.radius
        ship_hit(settings, screen, stats, sb, ship, aliens, bullets)
        create_alien(settings, screen, aliens)
    
    if stats.ships_left == 0:   
        pygame.mouse.set_visible(True)
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        stats.reset_stats()
        ship.center_ship()
        # Pause.
        sleep(0.5)
        sys.exit()
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(settings, stats, sb, screen, ship, aliens, bullets)
    check_ship_powerup_collisions(settings, screen, stats, sb, ship,
        aliens, bullets, powerups)

def check_aliens_bottom(settings, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            # sb.blood -= 1
            stats.score -= 1
            sb.prep_score()
            # Treat this the same as if the ship got hit.
            # ship_hit(settings, screen, stats, sb, ship, aliens, bullets)
            break 


def ship_hit(settings, screen, stats, sb, ship, aliens, bullets):    
    if sb.blood <= 0:  
        pygame.mixer.Sound('sounds/loss.wav').play()
        ship.hide()
        stats.ships_left -=1
        sb.prep_ships()
        stats.score = 0
        sb.prep_score()
        sb.show_score()
        sb.blood = 100
        sleep(0.8)

def check_ship_powerup_collisions(settings, screen, stats, sb, ship,
        aliens, bullets, powerups):
    collisions = pygame.sprite.spritecollide(ship, powerups, True)
    for col in collisions:
        pygame.mixer.Sound('sounds/powerup-beep.wav').play()
        ship.powerup() 

#redraws the screen on each pass through the main loop/ we need to modify update_screen() to
#make sure each bullet is redrawn to the screen before we call flip()  
def update_screen(settings, screen, stats, sb, ship, aliens, bullets, powerups):
    """Update images on the screen, and flip to the new screen."""
    background = pygame.image.load('assets/tree-background.jpg').convert()
    background_rect = background.get_rect()
    screen.fill(settings.bg_color)  ## draw the stargaze.png image
    screen.blit(background, background_rect)
    sb.energy_bar(screen, settings)
    #redraw all bullets behind ship and aliens
    #we loop through the sprites in bullets and call draw_bullet() on each one to draw
    #all the bullets to the screen.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    # #draw the ship on screen by calling ship.blitme(), blit() use to draw images to the screen
    ship.blitme()
    #In this case, aliens.draw(screen) draws each alien in the group to the screen.    
    aliens.draw(screen)

    for power in powerups.sprites():
        power.draw_powerup()

    #Make the most recently drawn screen visible. 
    #Draw the play button if the game is inactive
    sb.show_score() #draw the score info
    #show the new positions of elements and hide the old ones, creating
    #the illusion of smooth movement.    
    pygame.display.flip() 

