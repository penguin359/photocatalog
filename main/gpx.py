from lxml import etree

class GPXError(Exception):
	pass

class GPX:
	trackCount = 0
	author = ''

	def loadString(self, string):
		#if len(string) == 0:
		#	raise GPXError()
		try:
			doc = etree.fromstring(string)
		except etree.LxmlError as ex:
			print 'Food: ' + str(ex)
			raise GPXError('hi')

	def loadFile(self, file):
		self.author = 'Loren M. Lang'
