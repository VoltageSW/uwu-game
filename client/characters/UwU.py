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
from image.CharacterImage import CharacterImage
import pygame

class UwU:

	def __init__(self, main):
		self.main = main
		self.current_state = "idle_left"
		self.current_index = 0
		self.current_pos = [300, 0]
		self.idle_time = 500
		self.time = 0
		self.idle_left = [CharacterImage("UwU/1.png", self.current_pos), CharacterImage("UwU/2.png", self.current_pos)]
		self.idle_right = [CharacterImage("UwU/1.png", self.current_pos), CharacterImage("UwU/2.png", self.current_pos)]
		for image in self.idle_right:
			image.img = pygame.transform.flip(image.img, True, False)
		self.rect = pygame.Rect(self.current_pos, (32, 32))
		self.current_time = 0

	def loop(self):
		if pygame.time.get_ticks() - self.time > self.idle_time:
			if self.current_state == "idle_left":
				if self.current_index >= len(self.idle_left) - 1:
					self.current_index = 0
				else:
					self.current_index += 1
			else:
				if self.current_index >= len(self.idle_right) - 1:
					self.current_index = 0
				else:
					self.current_index += 1
			self.time = pygame.time.get_ticks()
		self.current_time = pygame.time.get_ticks()

		if self.current_state == "idle_left":
			self.main.window.blit(self.idle_left[self.current_index].img, self.rect)
		elif self.current_state == "idle_right":
			self.main.window.blit(self.idle_right[self.current_index].img, self.rect)
