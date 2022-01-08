import os
from sys import argv
import colorsys
import pygame
import time
import ctypes

def pos_def(dot_radius, dot_width):
	def hsv2rgb(h, s, v):
		return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
	pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (0, mouseY), (WIDTH, mouseY), width=dot_width)
	pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (mouseX, 0), (mouseX, HEIGHT), width=dot_width)
def getscreen_res():
	screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
	return str(screensize).replace("(", "").replace(" ", "").replace(")", "").split(",")

hue = 0
secs = 2
os.system("cls")
print(f"READ HARD ({secs} seconds): Press any key to exit in the GUI\nPlease forgive us about mouse scrolling, this is Special event")
pygame.init()
WIDTH = 600
HEIGHT = 400
APP_NAME = f"Mouse Pad {WIDTH}x{HEIGHT} [3.0] 3rd Gen"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)
bg = (77, 77, 77)
runtime = True
fnts = 20
font = pygame.font.SysFont('Consolas', fnts)
press = (255, 255, 0)
non_press = (0, 255, 255)
non_txt = (70, 70, 70)
argv.remove(argv[0])
x = WIDTH / 6
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
		scripts = ["Left Mouse Pressed at X:", "Wheel Mouse Pressed at X:", "Right Mouse Pressed at X:", "No Mouse Pressed at X:", "Mouse Scrolled at X:"]
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

