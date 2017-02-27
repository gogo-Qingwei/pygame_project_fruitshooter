import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats
        self.blood = stats.blood

        self.mini_ship = pygame.transform.scale(pygame.image.load('assets/player.png').convert_alpha(), (30,30))
        self.mini_ship.set_colorkey((0,0,0))
        
        #Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()

    def energy_bar(self, screen, settings):
        if self.blood< 0:
            self.blood = 0
        fill = (self.blood/100) * settings.bar_width
        pygame.draw.rect(screen, (255, 114, 96), pygame.Rect((settings.screen_width - settings.bar_width)/2, 52, fill, settings.bar_height))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect((settings.screen_width - settings.bar_width)/2, 52, settings.bar_width, 
                        settings.bar_height),2)

    def prep_score(self):
        """Turn the score into a rendered image."""
        # Display the score at the top right of the screen.
        text = str(int(round(self.stats.score, -1)))
        font_name = pygame.font.match_font('mono', bold=1)
        font = pygame.font.Font(font_name,32)
        self.text_screen = font.render(text, True, (255, 204, 0))
        self.score_rect = self.text_screen.get_rect()
        self.score_rect.left = self.screen_rect.left + 40
        self.score_rect.top = self.screen_rect.top + 30
        
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        text = str(int(round(self.stats.high_score, -1)))
        font_name = pygame.font.match_font('mono', bold=1)
        font = pygame.font.Font(font_name,32)
        self.text_high_screen = font.render(text, True, (102, 153, 102))        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.text_high_screen.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 40
        self.high_score_rect.top = self.screen_rect.top + 30
                
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.settings, self.screen, self.mini_ship)
            ship.rect.x = self.screen_rect.centerx+ship_number * ship.rect.width-40
            ship.rect.top = self.screen_rect.top + 12
            self.ships.add(ship)

        
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.text_screen, self.score_rect)
        self.screen.blit(self.text_high_screen, self.high_score_rect)
        self.ships.draw(self.screen)
 
