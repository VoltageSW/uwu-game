import pygame,random

class Particle:

	def __init__(self, main, to_pos):
		self.main = main
		self.to_pos = to_pos
		self.particles = []

	def spawnParticles(self):
		self.particles.append([[self.to_pos[0] + 7, self.to_pos[1] + 7], [random.randint(-20, 20) / 5, random.randint(0,20) / 5], 7])
		for particle in self.particles:
			particle[0][0] += particle[1][0]
			particle[0][1] += particle[1][1]
			particle[2] -= 0.2
			rect = pygame.draw.circle(self.main.window, (255,255,255), (particle[0][0], particle[0][1]), particle[2])
			if particle[2] <= 0:
				self.particles.remove(particle)
		self.to_pos = pygame.mouse.get_pos()