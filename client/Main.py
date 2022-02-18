import pygame, sys
import utils.ColorFormat as ColorFormat
from pygame.locals import *

class Main:

	def __init__(self):
		pygame.init()

		self.window = pygame.display.set_mode((500, 400), 0 , 32)
		pygame.display.set_caption('Magara Jam 4 Client')

		self.basicFont = pygame.font.SysFont(None, 48)

		pygame.display.update()

		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            pygame.quit()
		            sys.exit()
		    pygame.display.update()

main = Main()