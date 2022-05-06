from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from players.models import Players


class PlayersAdmin(ModelAdmin):
    pass


admin.site.register(Players, PlayersAdmin)
