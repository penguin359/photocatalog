from unittest import skip

from django.test import TestCase
from django.utils import timezone

from main.models import Track
from main.gpx import GPX, GPXException

class TrackModelTestCase(TestCase):
	def setup(self):
		pass

	def test_create_track(self):
		"""Can a Track Model be created"""
		#Track.objects.create(creation=timezone.now())
		Track.objects.create()

class GPXTestCase(TestCase):
	def test_load_gpx_string(self):
		gpx = GPX()
		gpx.loadString('<gpx/>')
		self.assertEqual(gpx.trackCount, 0)
		self.assertEqual(gpx.author, '')

	def test_load_empty_file(self):
		gpx = GPX()
		with self.assertRaises(GPXException):
			gpx.loadString('')

	def test_load_malformed_xml(self):
		gpx = GPX()
		with self.assertRaises(GPXException):
			gpx.loadString('<gpx><metadata></gpx>')

	@skip("Not implemented yet")
	def test_load_gpx_string_minimal(self):
		gpx = GPX()
		gpx.loadString('<gpx><metadata><name>GPS</name></metadata></gpx>')
		self.assertEqual(gpx.trackCount, 0)
		self.assertEqual(gpx.name, '')

	def test_load_gpx_file(self):
		gpx = GPX()
		gpx.loadFile('testdata/simple.gpx')
		self.assertEqual(gpx.trackCount, 0)
		self.assertEqual(gpx.author, 'Loren M. Lang')

	@skip("Not implemented yet")
	def test_load_gpx_file2(self):
		gpx = GPX()
		gpx.loadFile('testdata/simple2.gpx')
		self.assertEqual(gpx.trackCount, 0)
		self.assertEqual(gpx.author, 'John Doe')
