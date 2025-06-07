from django.contrib import admin
from .models import Location,Profile

class LocationAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location,LocationAdmin)
admin.site.register(Profile,ProfileAdmin)