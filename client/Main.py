"""
MIT License

Copyright (c) 2022 Voltage Software

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pygame, sys
import utils.ColorFormat as ColorFormat
from pygame.locals import *
from ui.MainMenuUI import MainMenuUI
from utils.Cursor import Cursor
from ui.CreditsUI import CreditsUI
from ui.FPS import FPS
from image.Image import Image
from particle.Particle import Particle
from characters.UwU import UwU
import json
from utils.TileLoader import TileLoader

class Main:

	def __init__(self):
		pygame.init()

		pygame.mouse.set_visible(False)

		self.cursor = Cursor(self)
		self.mousex, self.mousey = pygame.mouse.get_pos()
		self.click = False

		self.clock = pygame.time.Clock()

		self.windowx = 1024
		self.windowy = 728

		self.DISPLAY_SIZE = (800,600)

		self.window = pygame.Surface(self.DISPLAY_SIZE)
		self.display = pygame.display.set_mode((self.windowx, self.windowy), 0, 32)
		pygame.display.set_caption('UwU Game Client')

		self.programIcon = Image("voltagesoftwareicon.jpeg", (0,0))
		pygame.display.set_icon(self.programIcon.img)

		self.basicFont = pygame.font.SysFont(None, 48)

		self.mainmenu = MainMenuUI(self)

		pygame.display.update()

		self.mouse_particle = Particle(self, pygame.mouse.get_pos())

		self.background = Image("background1.png", (0,0))
		self.background.setScale(self.DISPLAY_SIZE)

		self.character = UwU(self)

		# UI

		self.credits_ui = CreditsUI(self)

		self.mainmenu.run()

		self.game_map = self.loadMap("maps/level1")

		self.gravity_y = 0

		self.move_left = False
		self.move_right = False

		self.tile_rects = []

		self.tile_loader = TileLoader(self)

		while True:
			self.window.fill(ColorFormat.BLACK)
			self.window.blit(self.background.img, (self.background.img_pos[0], self.background.img_pos[1]))
			self.gravity_y += 0.2
			if self.gravity_y >= 6:
				self.gravity_y = 6
			self.character.rect.y += self.gravity_y
			self.character.loop()
			self.tile_loader.loadTiles()
			self.fps_ui = FPS(self, self.clock.get_fps())
			self.cursor.initCursor()
			self.click = False
			if self.move_right:
				self.character.rect.x += 5
			if self.move_left:
				self.character.rect.x -= 5
			if self.character.rect.y >= self.DISPLAY_SIZE[1]:
				self.character.rect.y = 0
				self.character.rect.x = 50
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.mainmenu.active = True
						self.mainmenu.run()
					if event.key == K_a:
						self.move_left = True
						self.character.current_state = "idle_left"
					if event.key == K_d:
						self.move_right = True
						self.character.current_state = "idle_right"
					if event.key == K_w:
						self.gravity_y += -10
				if event.type == KEYUP:
					if event.key == K_a:
						self.move_left = False
					if event.key == K_d:
						self.move_right = False
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						self.click = True
			surf = pygame.transform.scale(self.window, (self.windowx, self.windowy))
			self.display.blit(surf, (0,0))
			pygame.display.update()
			self.clock.tick(60)

	def loadMap(self, map_name):
		level = open(map_name + ".json", "r")
		lvl = json.loads(level.read())
		level.close()
		return lvl

	def checkCollide(self, rect, rect2):
		if(rect.colliderect(rect2)):
			return True
		return False

def main():
	main = Main()

if __name__ == '__main__':
	main()
