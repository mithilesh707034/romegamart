from django.contrib import admin

from .models import *
admin.site.register((Seller,Buyer,Product,Maincategory,Category,Brand))
