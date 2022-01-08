import os
from sys import argv
import colorsys
import pygame
import time
import ctypes

def hsv2rgb(h, s, v):
	return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
hue = 0
def pos_def(dot_radius, dot_width):
	pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (0, mouseY), (WIDTH, mouseY), width=dot_width)
	pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (mouseX, 0), (mouseX, HEIGHT), width=dot_width)
def getscreen_res():
	user32 = ctypes.windll.user32
	screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	return str(screensize).replace("(", "").replace(" ", "").replace(")", "").split(",")

os.system("cls")
secs = 2
print(f"READ HARD ({secs} seconds): Press any key to exit in the GUI\nPlease forgive us about mouse scrolling, this is Special event");time.sleep(secs)
pygame.init()
WIDTH = int(getscreen_res()[0])
HEIGHT = int(getscreen_res()[1])
APP_NAME = f"Mouse Tracker FULL SCREEN [v2.9.9.8] .ver - The End of."
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)
bg = (100, 100, 100)
runtime = True
fnts = 25
font = pygame.font.SysFont('Consolas', fnts)
press = (255, 255, 0)
non_press = (0, 255, 255)
non_txt = (70, 70, 70)
argv.remove(argv[0])
x = WIDTH / 3
y = 10
y2 = 40
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
		scripts = [
		"Left Mouse Pressed at X:", #0
		"Wheel Mouse Pressed at X:", #1
		"Right Mouse Pressed at X:", #2
		"No Mouse Pressed at X:", #3
		"Mouse Scrolled at X:" #4
		]
		if mouseD[0]:
			screen.blit(font.render(f"{scripts[0]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		elif mouseD[1]:
			screen.blit(font.render(f"{scripts[1]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		elif mouseD[2]:
			screen.blit(font.render(f"{scripts[2]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		else:
			screen.blit(font.render(f"{scripts[3]} {mouseX}, Y: {mouseY}", True, non_press), (x, y))

		for event in pygame.event.get():
			if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN):
				runtime = False
			if event.type == pygame.MOUSEWHEEL:
				screen.blit(font.render(f"{scripts[4]} {mouseX}, Y: {mouseY}", True, press), (x, y+30))
		pygame.display.update()
		time.sleep(0.01)
		hue += 0.00079
		pygame.display.flip()
else:
	try:
		print(argv[y])
	except IndexError as ie:
		print(f"ERROR: NO ARGUMENTS: {ie}")
pygame.quit()

