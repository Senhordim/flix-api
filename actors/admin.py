from django.contrib import admin
from actors.models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'nationality', 'created_at', 'updated_at')

