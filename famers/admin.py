from django.contrib import admin
from .models import Farmer, Product, Subsidized

admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(Subsidized)