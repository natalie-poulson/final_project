from django.contrib import admin
from . import models
from django.contrib.gis.db import models as gismodels
from mapwidgets.widgets import GooglePointFieldWidget

class TripAdmin(admin.ModelAdmin):
    formfield_overrides = {
        gismodels.PointField: {"widget": GooglePointFieldWidget}
    }
    
admin.site.register(models.UserProfileInfo)
admin.site.register(models.Trip, TripAdmin)
admin.site.register(models.Post)
admin.site.register(models.Gear)
admin.site.register(models.Food)




# Register your models here.
