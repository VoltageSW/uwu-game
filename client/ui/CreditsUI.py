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
from pygame.locals import *
import utils.ColorFormat as ColorFormat
from ui.FPS import FPS

class CreditsUI:

	def __init__(self, main):
		self.main = main

	def run(self):
		while True:
			self.main.window.fill(ColorFormat.BLACK)
			self.main.fps_ui = FPS(self.main, self.main.clock.get_fps())
			self.main.mouse_particle.spawnParticles()
			self.main.cursor.initCursor()
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						return
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			self.main.clock.tick(60)
