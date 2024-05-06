from django.contrib import admin
from . import models

admin.site.register(models.RiddleModel)
admin.site.register(models.CreatorModel)