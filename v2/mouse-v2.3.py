from pygame import gfxdraw
from sys import argv
import pygame
pygame.init()
WIDTH = 600
HEIGHT = 400
APP_NAME = f"Mouse Tracker ({WIDTH}x{HEIGHT}) [v2.3]"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)
bg = (80, 80, 80)
runtime = True
font = pygame.font.SysFont('Consolas', 20)
press = (255, 255, 0)
non_press = (0, 255, 255)
non_txt = (70, 70, 70)
dot_color = (255, 0, 255)
argv.remove(argv[0])
x = 95
y = 10
dot = 2
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
			screen.blit(font.render(f"{scripts[0]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		elif mouseD[2]:
			screen.blit(font.render(f"{scripts[1]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		else:
			screen.blit(font.render(f"{scripts[2]} at X: {mouseX}, Y: {mouseY}", True, non_press), (x, y))
			screen.blit(font.render(f"{scripts[2]}", True, non_press), (x, y))

		pygame.draw.circle(screen, dot_color, (mouseX, mouseY), dot)
		pygame.draw.line(screen, dot_color, (0, mouseY), (WIDTH, mouseY), width=dot)
		pygame.draw.line(screen, dot_color, (mouseX, 0), (mouseX, HEIGHT), width=dot)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runtime = False
		pygame.display.update()
		pygame.display.flip()
else:
	try:
		print(argv[y])
	except IndexError as ie:
		print(f"ERROR: NO ARGUMENTS: {ie}")
pygame.quit()


