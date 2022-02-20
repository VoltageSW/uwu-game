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
class Cursor:

	def __init__(self, main, default_state = "cursor_default.png"):
		self.main = main
		self.default_cursor_dir = "assets/cursors/"
		self.default_state = default_state
		self.current_state = self.default_state

	def initCursor(self):
		self.cursor = pygame.image.load(self.default_cursor_dir + self.current_state)
		self.cursor = pygame.transform.scale(self.cursor, (15, 15))
		self.main.window.blit(self.cursor, pygame.mouse.get_pos())