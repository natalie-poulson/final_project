from django.contrib import admin
from . import models

admin.site.register(models.UserProfileInfo)
admin.site.register(models.Trip)
admin.site.register(models.Post)
admin.site.register(models.Gear)
admin.site.register(models.Food)


# Register your models here.
