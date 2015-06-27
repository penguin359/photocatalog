from lxml import etree

class GPXError(Exception):
	pass

class GPX:
	author = ''
	name = ''
	tracks = []

	# TODO Refractor XML extraction of text
	# TODO Add more GPX metadata
	def parseGPX(self, root):
		ns = { 'gpx': 'http://www.topografix.com/GPX/1/1' }
		if root.tag == 'gpx':
			ns = { 'gpx': '' }
		element = root.find('gpx:metadata/gpx:author/gpx:name', ns)
		if element != None:
			self.author = element.text
		element = root.find('gpx:metadata/gpx:name', ns)
		if element != None:
			self.name = element.text
		self.tracks = root.findall('gpx:trk', ns)

	def loadString(self, string):
		#if len(string) == 0:
		#	raise GPXError()
		try:
			root = etree.fromstring(string)
		except etree.LxmlError as ex:
			raise GPXError(ex)

		self.parseGPX(root)

	def loadFile(self, file):
		#self.author = 'Anonymous'
		try:
			doc = etree.parse(file)
		except etree.LxmlError as ex:
			raise GPXError(ex)

		self.parseGPX(doc.getroot())
