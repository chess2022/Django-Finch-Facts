from django.contrib import admin
from .models import Finch, Sighting, Region, Image

# Register your models here.
admin.site.register(Finch)
admin.site.register(Sighting)
admin.site.register(Region)
admin.site.register(Image)