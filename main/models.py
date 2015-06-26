from django.db import models

class Track(models.Model):
	name = models.CharField(max_length=30)
	comment = models.CharField(max_length=30, default='')
	description = models.CharField(max_length=30, default='')
	kind = models.CharField(max_length=30, default='')
	#creation = models.DateTimeField('Creation Time')
