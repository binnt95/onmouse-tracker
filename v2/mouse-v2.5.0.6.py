import os
from sys import argv
import colorsys
import pygame
import time

def hsv2rgb(h, s, v):
	return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
hue = 0
def pos_def(dot_radius, dot_width, color):
	pygame.draw.circle(screen, color, (mouseX, mouseY), dot_radius)
	pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (0, mouseY), (WIDTH, mouseY), width=dot_width)
	pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (mouseX, 0), (mouseX, HEIGHT), width=dot_width)

os.system("cls")
print("Press any key to exit")
pygame.init()
WIDTH = 1920
HEIGHT = 1080
APP_NAME = f"Mouse Tracker ({WIDTH}x{HEIGHT}) Full Screen [v2.5.0.6]"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)
bg = (80, 80, 80)
runtime = True
font = pygame.font.SysFont('Consolas', 30)
press = (255, 255, 0)
non_press = (0, 255, 255)
non_txt = (70, 70, 70)
dot_color = (255, 255, 255)
argv.remove(argv[0])
x = 630
y = 10
dot_radius = 4
dot_width = 2
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

		pos_def(dot_radius, dot_width, dot_color)

		for event in pygame.event.get():
			if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN):
				runtime = False
		pygame.display.update()
		time.sleep(0.01)
		hue += 0.01
		pygame.display.flip()
else:
	try:
		print(argv[y])
	except IndexError as ie:
		print(f"ERROR: NO ARGUMENTS: {ie}")
pygame.quit()


