from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from . import models

admin.site.register(models.UserProfileInfo)
admin.site.register(models.Trip, LeafletGeoAdmin)
admin.site.register(models.Post)
admin.site.register(models.Gear)
admin.site.register(models.Food)


# Register your models here.
