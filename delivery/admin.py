from django.contrib import admin
from .models import Products, Types, Addreses

class ProductsAdmin(admin.ModelAdmin):
    model = Products


class TypesAdmin(admin.ModelAdmin):
    model = Products


class AdressesAdmin(admin.ModelAdmin):
    model = Products


admin.site.register(Products, ProductsAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(Addreses, AdressesAdmin)