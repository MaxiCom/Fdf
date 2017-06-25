from pygame.locals import *
import pygame

X_START = 400
Y_START = 20

TILE_WIDTH = 40
TILE_HEIGHT = 25

class Window:
	def populateMap(self, map):
		try:
			for i1, y in enumerate(map):
				for i2, x in enumerate(y):
					x_point = (i2 - i1) * (TILE_WIDTH / 2) + X_START + int(x)
					y_point = (i2 + i1) * (TILE_HEIGHT / 2) + Y_START - int(x)

					pygame.draw.circle(self._display_surf, (0, 255, 0), (x_point, y_point), 1)
					
					if i2 < len(y) - 1:
						x_next_point = (i2 + 1 - i1) * (TILE_WIDTH / 2) + X_START + int(map[i1][i2 + 1])
						y_next_point = (i2 + 1 + i1) * (TILE_HEIGHT / 2) + Y_START - int(map[i1][i2 + 1])
						
						pygame.draw.line(self._display_surf, (0, 255, 0), (x_point, y_point), (x_next_point, y_next_point))
					
					if i1 < len(map) - 1:
						x_next_point = (i2 - 1 - i1) * (TILE_WIDTH / 2) + X_START + int(map[i1 + 1][i2])
						y_next_point = (i2 + 1 + i1) * (TILE_HEIGHT / 2) + Y_START - int(map[i1 + 1][i2])
							
						pygame.draw.line(self._display_surf, (0, 255, 0), (x_point, y_point), (x_next_point, y_next_point))

		except Exception as e:
			print '\033[31m%s\033[m' % (e)

	def displayMap(self, map):
		self._running = True
		self._size = (1000, 600)
		self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self.populateMap(map);
		
		pygame.display.set_caption('Fdf')
		pygame.init()

		while self._running:
			try:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self._running = False
					elif event.type == pygame.KEYDOWN:
						if event.key == 27:
							self._running = False
				pygame.display.flip()
			except KeyboardInterrupt:
				self._running = False

		pygame.quit()