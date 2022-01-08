from pygame import gfxdraw
from sys import argv
import colorsys
import pygame
import time
import os

def hsv2rgb(h, s, v):
	return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
hue = 0
def pos_def(dot_radius, dot_width):
	pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (0, mouseY), (WIDTH, mouseY), width=dot_width)
	pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (mouseX, 0), (mouseX, HEIGHT), width=dot_width)

os.system("cls")
print("Press \"Delete\" key to exit")
pygame.init()
WIDTH = 600
HEIGHT = 400
APP_NAME = f"Mouse Tracker ({WIDTH}x{HEIGHT}) [v2.8.1]"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)
bg = (80, 80, 80)
runtime = True
font = pygame.font.SysFont('Consolas', 20)
press = (255, 255, 0)
non_press = (0, 255, 255)
non_txt = (70, 70, 70)
argv.remove(argv[0])
x = 95
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
		pos_def(dot_radius, dot_width)
		scripts = ["Left Mouse Pressed at X:", "Right Mouse Pressed at X: ", "No Mouse Pressed"]
		if mouseD[0]:
			screen.blit(font.render(f"{scripts[0]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		elif mouseD[2]:
			screen.blit(font.render(f"{scripts[1]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		else:
			screen.blit(font.render(f"{scripts[2]} at X: {mouseX}, Y: {mouseY}", True, non_press), (x, y))
			screen.blit(font.render(f"{scripts[2]}", True, non_press), (x, y))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runtime = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DELETE:
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


