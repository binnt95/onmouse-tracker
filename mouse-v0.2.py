import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse pad First Release [v0.2] (Pre-Compiled: Friday, December 24th, 2021 21 century), size: 800x600")
runtime = True
while runtime:
	mouseX, mouseY = pygame.mouse.get_pos()
	screen.fill((80, 80, 80))
	screen.blit(pygame.font.SysFont('Consolas', 20).render(str(mouseX) + "," + str(mouseY), True, (255, 255, 255)), (10, 10))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runtime = False
	pygame.display.update()
	pygame.display.flip()
pygame.quit()