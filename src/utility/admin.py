from django.contrib import admin
from django.apps import apps

from music import models
from utility.forms import FileAdminForm

app = apps.get_app_config('utility')

for model_name, model in app.models.items():
	if model_name not in ['file', ]:
		admin.site.register(model)


@admin.register(models.File)
class PlanAdmin(admin.ModelAdmin):
	form = FileAdminForm
