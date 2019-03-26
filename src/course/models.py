from django.db import models

from utility.models import File


class Narrator(models.Model):
	name = models.CharField(max_length=256)
	artwork = models.ForeignKey(File, on_delete=models.PROTECT)

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=256)
	description = models.TextField(null=True, blank=True)
	artwork = models.ForeignKey(File, on_delete=models.PROTECT)

	def __str__(self):
		return self.name


class Chapter(models.Model):
	name = models.CharField(max_length=256)
	artwork = models.ForeignKey(File, on_delete=models.PROTECT)
	narrator = models.ForeignKey(Narrator, on_delete=models.CASCADE, related_name='chapters')

	def __str__(self):
		return self.name


class Course(models.Model):
	name = models.CharField(max_length=256)
	files = models.ManyToManyField(File, related_name='courses', verbose_name='Course file')
	artwork = models.ForeignKey(File, on_delete=models.PROTECT, related_name='course_artwork')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='courses')

	def __str__(self):
		return self.name
