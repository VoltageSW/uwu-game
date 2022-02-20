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
from menu.actions.CreditsAction import CreditsAction
from menu.actions.SinglePlayerAction import SinglePlayerAction

class Menu:

	def __init__(self, ui, main):
		self.main = main
		self.ui = ui

	def initMenu(self):
		# Background Image
		background = Image("background_menu.png", (0, 0))
		background.setScale((self.main.DISPLAY_SIZE[0], self.main.DISPLAY_SIZE[1]))
		self.main.window.blit(background.img, (background.img_pos[0], background.img_pos[1]))

		icon = Image("voltagesoftwareicon.jpeg", (0, 0))
		icon.setScale((64,64))
		icon_rect = icon.img.get_rect()
		icon_rect.x = self.main.DISPLAY_SIZE[0] - (icon_rect.width + 5)
		icon_rect.y = self.main.DISPLAY_SIZE[1] - (icon_rect.height + 5)
		self.main.window.blit(icon.img, icon_rect)

		icon_text = self.main.basicFont.render('github.com/VoltageSW', True, ColorFormat.WHITE)
		icon_text_rect = icon_text.get_rect()
		icon_text_rect.right = icon_rect.left - 15
		icon_text_rect.y = icon_rect.y + icon_text_rect.height / 2
		self.main.window.blit(icon_text, icon_text_rect)

		self.title = "UwU Game"
		title_font = pygame.font.SysFont(None, 60, True, True)
		title_text = title_font.render(self.title, True, ColorFormat.YELLOW)
		title_rect = title_text.get_rect()
		title_rect.x = 30
		title_rect.y = self.main.DISPLAY_SIZE[1] // 2
		self.main.window.blit(title_text, title_rect)

		singleplayer_btn = MenuText(
			self.main,
			self.main.basicFont,
			"Singleplayer",
			True,
			ColorFormat.WHITE,
			(30, (self.main.DISPLAY_SIZE[1] // 2) + 50),
			None,
			True,
			SinglePlayerAction(self.ui, self.main)
		)
		multiplayer_btn = MenuText(
			self.main,
			self.main.basicFont,
			"Multiplayer",
			True,
			ColorFormat.GRAY,
			(30, (self.main.DISPLAY_SIZE[1] // 2) + 85),
			None,
			False
		)
		credits_btn = MenuText(
			self.main,
			self.main.basicFont,
			"Credits",
			True,
			ColorFormat.WHITE,
			(30, (self.main.DISPLAY_SIZE[1] // 2) + 115),
			None,
			True,
			CreditsAction(self.main)
		)
		exit_btn = MenuText(
			self.main,
			self.main.basicFont,
			"Exit",
			True,
			ColorFormat.WHITE,
			(30, (self.main.DISPLAY_SIZE[1] // 2) + 145),
			None,
			True,
			ExitAction()
		)

		singleplayer_btn.initText()
		multiplayer_btn.initText()
		credits_btn.initText()
		exit_btn.initText()
