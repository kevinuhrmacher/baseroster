from django.contrib import admin
from roster.models import Player
from roster.models import Coach

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
class CoachAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Player, PlayerAdmin)
admin.site.register(Coach, CoachAdmin)