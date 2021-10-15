from django.contrib import admin
from .models import Products, Ingredient, ProductsRecipe, IngredientsPresent


@admin.register(Products, Ingredient, ProductsRecipe, IngredientsPresent)
class ProductsAdmin(admin.ModelAdmin):
    pass
