from django.urls import path

from .views import list_all_products, add_ingredients, add_products, list_all_ingredients, list_all_products_recipe, \
    update_product, delete_product, list_ingredient, update_ingredient, delete_ingredient

app_name = 'products'

urlpatterns = [
    path('products/all', list_all_products, name="products_all"),
    path('product/update', update_product, name="products_add_photo"),
    path('product/<slug:id>', list_all_products_recipe, name="product"),
    path('product/delete/<slug:id>', delete_product, name="products_add_photo"),
    path('ingredients/all', list_all_ingredients, name="ingredient_all"),
    path('ingredient/add', add_ingredients, name="ingredient_add"),
    path('ingredient/update', update_ingredient, name="ingredient_add"),
    path('ingredient/<slug:id>', list_ingredient, name="product"),
    path('ingredient/delete/<slug:id>', delete_ingredient, name="products_add_photo"),
    path('products/add', add_products, name="products_add"),
]
