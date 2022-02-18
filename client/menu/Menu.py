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
import utils.ColorFormat as ColorFormat
from image.Image import Image
from menu.MenuText import MenuText
import pygame
from menu.actions.ExitAction import ExitAction

class Menu:

	def __init__(self, main):
		self.main = main

	def initMenu(self):
		# Background Image
		background = Image("background_menu.png", (0, 0))
		background.setScale((self.main.windowx, self.main.windowy))
		self.main.window.blit(background.img, (background.img_pos[0], background.img_pos[1]))

		self.title = "MAGARA JAM 4"
		title_font = pygame.font.SysFont(None, 60, True, True)
		title_text = title_font.render(self.title, True, ColorFormat.YELLOW)
		title_rect = title_text.get_rect()
		title_rect.x = 30
		title_rect.y = self.main.windowy // 2
		self.main.window.blit(title_text, title_rect)

		singleplayer_btn = MenuText(
			self.main,
			self.main.basicFont,
			"Singleplayer",
			True,
			ColorFormat.WHITE,
			(30, (self.main.windowy // 2) + 50),
		)
		multiplayer_btn = MenuText(
			self.main,
			self.main.basicFont,
			"Multiplayer",
			True,
			ColorFormat.GRAY,
			(30, (self.main.windowy // 2) + 85),
			None,
			False
		)
		credits_btn = MenuText(
			self.main,
			self.main.basicFont,
			"Credits",
			True,
			ColorFormat.WHITE,
			(30, (self.main.windowy // 2) + 115),
		)
		exit_btn = MenuText(
			self.main,
			self.main.basicFont,
			"Exit",
			True,
			ColorFormat.WHITE,
			(30, (self.main.windowy // 2) + 145),
			None,
			True,
			ExitAction()
		)

		singleplayer_btn.initText()
		multiplayer_btn.initText()
		credits_btn.initText()
		exit_btn.initText()