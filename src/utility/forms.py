import os
import uuid

from django import forms
from django.conf import settings

from music import models


class FileAdminForm(forms.ModelForm):
	file = forms.FileField()

	class Meta:
		model = models.File
		fields = ['file']

	def save(self, commit=True):
		super(FileAdminForm, self).save(commit=commit)
		f = self.files['file']
		file_name = '%s.%s' % (uuid.uuid4(), f.name.split('.')[-1])
		save_dir = os.path.join(settings.STATIC_BASE, settings.UPLOAD_TO)
		if not os.path.exists(save_dir):
			os.makedirs(save_dir)

		save_dir = os.path.join(save_dir, file_name)

		with open(save_dir, 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)

		self.instance.name = file_name
		self.instance.address = os.path.join('static', settings.UPLOAD_TO, file_name)
		self.instance.file_type = f.content_type
		self.instance.save()

		return self.instance
