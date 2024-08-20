from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'rating', 'movie', 'created_at', 'updated_at')
