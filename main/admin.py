from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    pass
