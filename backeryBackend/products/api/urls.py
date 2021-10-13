from django.urls import path

from .views import list_all_products, add_ingredients, add_products

app_name = 'products'

urlpatterns = [
    path('products/all', list_all_products, name="products_all"),
    path('ingredient/add', add_ingredients, name="ingredient_add"),
    path('products/add', add_products, name="products_add"),
]
