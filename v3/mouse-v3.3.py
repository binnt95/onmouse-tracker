#!/usr/bin/env python

import os
import colorsys
import pygame
import time
import ctypes

def main():
	def pos_def(dot_width):
		def hsv2rgb(h, s, v):
			return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
		pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (0, mouseY), (WIDTH, mouseY), width=dot_width)
		pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (mouseX, 0), (mouseX, HEIGHT), width=dot_width)
	def getscreen_res():
		screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
		return str(screensize).replace("(", "").replace(" ", "").replace(")", "").split(",")
	hue = 0
	secs = 0.01
	os.system("cls")
	print("Logo Copyright (c) Mojang Studios 2009 - 2022")
	time.sleep(secs)
	pygame.init()
	secs = 2
	runtime = True
	VERSION = 3.3
	WIDTH = 800
	HEIGHT = round(int(WIDTH / 4 * 3))
	APP_NAME = f"Mouse Pad {WIDTH}x{HEIGHT} [{VERSION}] 3rd gen"
	fnts = 26
	x = WIDTH / 6
	y = 10
	y2 = 40
	bg = (110, 110, 110)
	press = (255, 255, 0)
	non_press = (0, 255, 255)
	non_txt = (70, 70, 70)
	dot_width = 1
	mpos = []
	fullcheck = False
	mode = pygame.RESIZABLE
	while runtime:
		screen = pygame.display.set_mode((WIDTH, HEIGHT), mode)
		pygame.display.set_caption(APP_NAME)
		pygame.display.set_icon(pygame.image.load("apple.png").convert_alpha())
		font = pygame.font.SysFont('Consolas', fnts)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runtime = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					runtime = False
				if event.key == pygame.K_F11:
					fullcheck = not fullcheck
					if fullcheck:
						org_res = [WIDTH, HEIGHT]
						WIDTH = int(getscreen_res()[0])
						HEIGHT = int(getscreen_res()[1])
						bn = APP_NAME
						APP_NAME = f"Mouse Pad FULL SCREEN, Resolution: {WIDTH}x{HEIGHT} [{VERSION}] 3rd gen"
						bx = x
						x = WIDTH / 3
						bf = fnts
						fnts = 30
						time.sleep(secs-0.5)
						bm = mode
						mode = pygame.FULLSCREEN
					else:
						WIDTH = org_res[0]
						HEIGHT = org_res[1]
						APP_NAME = bn
						x = bx
						fnts = bf
						time.sleep(secs-0.5)
						mode = bm
						pygame.display.set_icon(pygame.image.load("apple.png").convert_alpha())

			if event.type == pygame.MOUSEWHEEL:
				screen.blit(font.render(f"{scripts[4]} {mouseX}, Y: {mouseY}", True, press), (x, y+30))

		mouseX, mouseY = pygame.mouse.get_pos()
		screen.fill((bg))
		txtR = font.render(f"{mouseX}, {mouseY}", True, bg)
		txtS = 10, 10
		screen.blit(txtR, txtS)
		mouseD = pygame.mouse.get_pressed()
		pos_def(dot_width)
		scripts = ["Left Mouse Pressed at X:", "Wheel Mouse Pressed at X:", "Right Mouse Pressed at X:", "No Mouse Pressed at X:", "Mouse Scrolled at X:"]
		if mouseD[0]:
			screen.blit(font.render(f"{scripts[0]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		elif mouseD[1]:
			screen.blit(font.render(f"{scripts[1]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		elif mouseD[2]:
			screen.blit(font.render(f"{scripts[2]} {mouseX}, Y: {mouseY}", True, press), (x, y))
		else:
			screen.blit(font.render(f"{scripts[3]} {mouseX}, Y: {mouseY}", True, non_press), (x, y))

		pygame.display.update()
		time.sleep(0.01)
		hue += 0.00099
		pygame.display.flip()
	pygame.quit()

if __name__ == '__main__':
	main()