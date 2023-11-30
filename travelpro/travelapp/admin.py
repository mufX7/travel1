from django.contrib import admin
from .models import place
admin.site.register(place)
def __str__(self):
    return self.name

from .models import team
admin.site.register(team)
def __str__(self):
    return self.name
