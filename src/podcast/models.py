from django.db import models

from utility.models import File


class Season(models.Model):
	name = models.CharField(max_length=256)
	artwork = models.ForeignKey(File, on_delete=models.PROTECT)

	def __str__(self):
		return self.name


class Podcast(models.Model):
	name = models.CharField(max_length=256)
	file = models.ForeignKey(File, related_name='podcasts', verbose_name='Podcast file', on_delete=models.PROTECT)
	artwork = models.ForeignKey(File, on_delete=models.PROTECT)
	chapter = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='podcasts')

	def __str__(self):
		return self.name
