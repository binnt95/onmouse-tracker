from sys import argv
import pygame
pygame.init()
WIDTH = 500
HEIGHT = 100
APP_NAME = f"Mouse Tracker ({WIDTH}x{HEIGHT}) [v1.7]"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)
bg = (80, 80, 80)
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
		txtR = font.render(f"{mouseX}, {mouseY}", True, bg)
		txtS = 10, 10
		screen.blit(txtR, txtS)
		mouseD = pygame.mouse.get_pressed()
		scripts = ["Left Mouse Pressed at X:", "Right Mouse Pressed at X: ", "No Mouse Pressed"]
		if mouseD[0]:
			screen.blit(font.render(f"{scripts[0]} {mouseX}, Y: {mouseY}", True, press), (55, 10))
		elif mouseD[2]:
			screen.blit(font.render(f"{scripts[1]} {mouseX}, Y: {mouseY}", True, press), (55, 10))
		else:
			screen.blit(font.render(f"{scripts[2]} at X: {mouseX}, Y: {mouseY}", True, non_press), (55, 10))
			screen.blit(font.render(f"{scripts[2]}", True, non_press), (55, 10))
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