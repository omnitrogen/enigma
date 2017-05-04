import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

#fond
fond = pygame.image.load("splash.png").convert()
fenetre.blit(fond, (0,0))

#perso
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#refresh
pygame.display.flip()

continuer = 1
pygame.key.set_repeat(1, 1)
while continuer:
	a = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
			
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				position_perso = position_perso.move(0,3)
			if event.key == K_UP:
				position_perso = position_perso.move(0,-3)
			if event.key == K_RIGHT:
				position_perso = position_perso.move(3,0)
			if event.key == K_LEFT:
				position_perso = position_perso.move(-3,0)
		if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 100:
			print("Zone dangereuse")
			
		if (a[0] > position_perso[0]):
			position_perso = position_perso.move(3,0)
		if (a[0] < position_perso[0]):
			position_perso = position_perso.move(-3,0)
		if (a[1] > position_perso[1]):
			position_perso = position_perso.move(0,3)
		if (a[1] < position_perso[1]):
			position_perso = position_perso.move(0,-3)
			
		if event.type == MOUSEMOTION:
			if (event.pos[0] > position_perso[0]):
				position_perso = position_perso.move(3,0)
			if (event.pos[0] < position_perso[0]):
				position_perso = position_perso.move(-3,0)
			if (event.pos[1] > position_perso[1]):
				position_perso = position_perso.move(0,3)
			if (event.pos[1] < position_perso[1]):
				position_perso = position_perso.move(0,-3)
				
	fenetre.blit(fond, (0,0))	
	fenetre.blit(perso, position_perso)

	pygame.display.flip()

