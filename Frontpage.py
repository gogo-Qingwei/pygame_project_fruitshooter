import sys
import pygame

def title_page(screen, settings):
	#music and music loop
	menu_song = pygame.mixer.music.load('sounds/Epoq-Lepidoptera.ogg')
	pygame.mixer.music.play(-1)
	#front images and position
	frontpage = pygame.image.load("assets/main.jpg").convert()
	frontpage = pygame.transform.scale(frontpage,
        (settings.screen_width,settings.screen_height), screen)

	screen.blit(frontpage,(0,0))
	pygame.display.update()

	while True:
		#poll() retrieves only a single event
		eventpoll = pygame.event.poll()
		if eventpoll.type == pygame.KEYDOWN:
			if eventpoll.key == pygame.K_RETURN:
				break
			elif eventpoll.key == pygame.K_ESCAPE:
				sys.exit()
		else:
			text_button(screen, "Press [ENTER] To Begin", 32, settings.screen_width/2,
						settings.screen_height/2-25)
			text_button(screen, "Press [ESC] To Quit", 32, settings.screen_width/2,
						settings.screen_height/2)
			pygame.display.update()

    #make music stop
	readypage = pygame.image.load("assets/readybar.jpg").convert()
	readypage = pygame.transform.scale(readypage,
        (settings.screen_width,settings.screen_height), screen)
	screen.blit(readypage,(0,0))
	pygame.display.update()
	pygame.mixer.music.stop()

def text_button(surf, text, size, x, y):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(pygame.font.match_font('font/PTN55F.ttf'), size)
    text_surface = font.render(text, True, (189,179,137))   ## True denotes the font to be anti-aliased 
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)