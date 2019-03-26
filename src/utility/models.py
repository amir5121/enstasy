from django.conf import settings
from django.db import models

from utility import constants


class File(models.Model):
	address = models.FilePathField(
		max_length=256, null=False, blank=False, verbose_name='address', path=settings.STATIC_URL)
	file_type = models.CharField(max_length=16, null=False, blank=False, choices=constants.FILE_TYPE)
	name = models.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
		print(self.name, self.get_file_type_display(), self.address)
		return self.get_file_type_display() + ' ' + self.name + " " + self.address
