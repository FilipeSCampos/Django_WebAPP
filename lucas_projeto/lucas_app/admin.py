from django.contrib import admin
from .models import CustomUser, Game, GameSpecifications

admin.site.register(CustomUser)
admin.site.register(Game)
admin.site.register(GameSpecifications)
