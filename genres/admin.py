from django.contrib import admin

from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

