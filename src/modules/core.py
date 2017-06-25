from modules.window import Window

class Core:
	_map_path = ''
	_map = []

	def __init__(self):
		self.window = Window()

	def getMap(self):
		try:
			with open(self._map_path, 'r') as file:
				map = file.read().strip().split('\n')

				for index, line in enumerate(map):
					self._map.append(line.split(' '))
					self._map[index] = filter(None, self._map[index])
		except Exception as e:
			print '\033[31m%s\033[m' % (e)

	def loadMap(self, map_path):
		self._map_path = map_path
		self.getMap()
		self.window.displayMap(self._map)