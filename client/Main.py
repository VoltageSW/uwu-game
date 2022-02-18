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
from menu.Menu import Menu
from utils.Cursor import Cursor
from ui.CreditsUI import CreditsUI
from ui.FPS import FPS

class Main:

	def __init__(self):
		pygame.init()

		pygame.mouse.set_visible(False)

		self.cursor = Cursor(self)
		self.mousex, self.mousey = pygame.mouse.get_pos()
		self.click = False

		self.fps_max = 60
		self.clock = pygame.time.Clock()

		self.windowx = 1024
		self.windowy = 628
		self.window = pygame.display.set_mode((self.windowx, self.windowy), 0, 32)
		pygame.display.set_caption('Magara Jam 4 Client')

		self.basicFont = pygame.font.SysFont(None, 48)

		self.menu = Menu(self)

		pygame.display.update()

		while True:
			self.menu.initMenu()
			self.fps_ui = FPS(self, self.clock.get_fps())
			self.cursor.initCursor()
			self.click = False
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						self.click = True
			pygame.display.update()
			self.clock.tick(self.fps_max)

def main():
	main = Main()

if __name__ == '__main__':
	main()