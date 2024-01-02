from django.contrib import admin
from .models import BuyDevice, BuyBrand


admin.site.register(BuyBrand)
admin.site.register(BuyDevice)