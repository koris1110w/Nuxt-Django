from django.contrib import admin
from . import models
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(models.RiddleModel, MarkdownxModelAdmin)
admin.site.register(models.CreatorModel)
admin.site.register(models.ReviewModel)