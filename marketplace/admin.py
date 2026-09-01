from django.contrib import admin
from .models import Artisan, Craft, Auction


admin.site.register(Artisan)
admin.site.register(Craft)
admin.site.register(Auction)