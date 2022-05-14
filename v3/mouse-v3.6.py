#!/usr/bin/env python

import io
import os
import time
import ctypes
import base64
import random
import pygame
import colorsys
import datetime

def main():
	def pos_def(dot_width):
		def hsv2rgb(h, s, v):
			return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
		pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (0, mouseY), (WIDTH, mouseY), width=dot_width)
		pygame.draw.line(screen, hsv2rgb(hue, 1, 1), (mouseX, 0), (mouseX, HEIGHT), width=dot_width)
	def getscreen_res():
		screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
		return str(screensize).replace("(", "").replace(" ", "").replace(")", "").split(",")
	def getimage_ba64(image):
		return pygame.image.load(io.BytesIO(base64.b64decode(image)))
	def getsort_num(n):
		n = str(n)
		sortn = n.split(".")[0]
		if sortn == "1":
			return "1st"
		if sortn == "2":
			return "2nd"
		if sortn == "3":
			return "3rd"
		else:
			return f"{sortn}th"

	hue = 0
	secs = 0.01
	os.system("cls")
	cyear = datetime.date.today().strftime("%Y")
	print(f"Logo Copyright (c) Mojang Studios 2009 - {cyear}")
	time.sleep(secs)
	pygame.init()
	secs = 2
	runtime = True
	VERSION = 3.6
	WIDTH = 800
	HEIGHT = round(int(WIDTH / 4 * 3))
	APP_NAME = f"Mouse Pad {WIDTH}x{HEIGHT} [{VERSION}] {getsort_num(VERSION)} gen"
	fnts = 26
	x = WIDTH / 6
	y = 10
	y2 = 40
	bg = (110, 110, 110)
	press = (255, 255, 0)
	non_press = (0, 255, 255)
	non_txt = (70, 70, 70)
	dot_width = 2
	mpos = []
	fullcheck = False
	mode = pygame.RESIZABLE
	icons = [
	'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAq0lEQVQ4y2NgoAco1WD6T7bmOnO+/yEqnP/pa/scAfH/IAzSDLIdRBNlEEjTFmG5//+nzQXTIM0gsbviqmA+XoPgmmW0//+PywQbAscgPlAcryEoBmDBIFcgG4LTAJhCZBqGYfwQTr7/WEMbZADMEJi/YXyY64gyABkjGwTzAlYDsLkCm0E4NcMMgIUFNu+A5PAaAAIgBTBDYAmKaM3IhsDiG5wagXyiNZMKANOS2s9rfvFXAAAAAElFTkSuQmCC'
	]

	while runtime:
		screen = pygame.display.set_mode((WIDTH, HEIGHT), mode)
		pygame.display.set_caption(APP_NAME)
		pygame.display.set_icon(getimage_ba64(icons[0]).convert_alpha())
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