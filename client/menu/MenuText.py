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
import pygame
import utils.ColorFormat as ColorFormat

class MenuText:

	def __init__(self, main, font, txt, antialias, color, size, background=None, active = True, action = None):
		self.main = main
		self.display = self.main.window
		self.font = font
		self.txt = txt
		self.antialias = antialias
		self.color = color
		self.default_color = self.color
		self.size = size
		self.background = background
		self.active = active
		self.action = action

	def initText(self):
		self.text = self.font.render(self.txt, self.antialias, self.color, self.background)
		self.rect = self.text.get_rect()
		self.rect[0] = self.size[0]
		self.rect[1] = self.size[1]
		if(self.checkCollide(pygame.mouse.get_pos())):
			if(self.active):
				if(self.main.click):
					if(self.action):
						self.action.doAction()
				self.color = ColorFormat.YELLOW
		else:
			self.color = self.default_color
		self.text = self.font.render(self.txt, self.antialias, self.color, self.background)
		self.display.blit(self.text, self.rect)

	def checkCollide(self, pos):
		if(self.rect.collidepoint(pos)):
			return True
		return False