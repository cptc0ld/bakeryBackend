from django.contrib import admin
from .models import Products, Ingredients


@admin.register(Products, Ingredients)
class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
