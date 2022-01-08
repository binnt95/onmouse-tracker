from sys import argv
import pygame
pygame.init()
APP_NAME = "Mouse Tracker (800x600) [v1.0.5.7]"
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)
bg = (80, 80, 80)
txt = (255, 255, 255)
runtime = True
font = pygame.font.SysFont('Consolas', 20)
press = (255, 255, 0)
non_press = (0, 255, 255)
non_txt = (70, 70, 70)
argv.remove(argv[0])
if not argv:
	while runtime:
		mouseX, mouseY = pygame.mouse.get_pos()
		screen.fill((bg))
		txtR = font.render(f"{mouseX}, {mouseY}", True, non_txt)
		txtS = 10, 10
		screen.blit(txtR, txtS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runtime = False
		pygame.display.update()
		pygame.display.flip()
else:
	try:
		print(argv[10])
	except IndexError as ie:
		print(f"ERROR: NO ARGUMENTS: {ie}")
pygame.quit()