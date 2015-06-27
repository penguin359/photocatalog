from unittest import skip

from django.test import TestCase
from django.utils import timezone

from main.models import Track
from main.gpx import GPX, GPXError

class TrackModelTestCase(TestCase):
	def setup(self):
		pass

	def test_create_track(self):
		"""Can a Track Model be created"""
		#Track.objects.create(creation=timezone.now())
		Track.objects.create()

class GPXTestCase(TestCase):
	# TODO Refractor to move all common asserts to helper function
	# TODO Fix dependency on hard-coded file paths
	def test_load_gpx_string(self):
		gpx = GPX()
		gpx.loadString('<gpx/>')
		self.assertEqual(gpx.author, '')
		self.assertEqual(gpx.name, '')
		self.assertEqual(len(gpx.tracks), 0)

	def test_load_empty_file(self):
		gpx = GPX()
		with self.assertRaises(GPXError):
			gpx.loadString('')

	def test_load_malformed_xml(self):
		gpx = GPX()
		with self.assertRaises(GPXError):
			gpx.loadString('<gpx><metadata></gpx>')

	def test_load_gpx_string_minimal(self):
		gpx = GPX()
		gpx.loadString('<gpx><metadata><name>GPS</name></metadata></gpx>')
		self.assertEqual(gpx.author, '')
		self.assertEqual(gpx.name, 'GPS')
		self.assertEqual(len(gpx.tracks), 0)

	def test_load_gpx_string_full_metadata(self):
		gpx = GPX()
		gpx.loadString('<gpx><metadata><name>GPS</name><author><name>Jimmy</name></author></metadata></gpx>')
		self.assertEqual(gpx.author, 'Jimmy')
		self.assertEqual(gpx.name, 'GPS')
		self.assertEqual(len(gpx.tracks), 0)

	# XXX Do I really care able duplicates when it fails reasonably?
	#def test_load_gpx_duplicate_metadata(self):
	#	gpx = GPX()
	#	gpx.loadString('<gpx><metadata><name>GPS</name></metadata><metadata><name>GPS4</name></metadata></gpx>')
	#	self.assertEqual(gpx.author, '')
	#	self.assertEqual(gpx.name, 'GPS')
	#	self.assertEqual(len(gpx.tracks), 0)

	def test_load_gpx_string_one_track(self):
		gpx = GPX()
		gpx.loadString('<gpx><metadata><name>Fun</name></metadata><trk/></gpx>')
		self.assertEqual(gpx.author, '')
		self.assertEqual(gpx.name, 'Fun')
		self.assertEqual(len(gpx.tracks), 1)

	def test_load_gpx_file(self):
		gpx = GPX()
		gpx.loadFile('main/testdata/simple.gpx')
		self.assertEqual(gpx.author, 'Anonymous')
		self.assertEqual(gpx.name, 'First test')
		self.assertEqual(len(gpx.tracks), 0)

	#@skip("Not implemented yet")
	def test_load_gpx_file2(self):
		gpx = GPX()
		gpx.loadFile('main/testdata/simple2.gpx')
		self.assertEqual(gpx.author, 'John Doe')
		self.assertEqual(gpx.name, 'Second test')
		self.assertEqual(len(gpx.tracks), 1)
