from rest_framework import serializers

from ..models import Products, Ingredients


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'ingredientsPresent']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['name', 'quantityPresent', 'costPrice']
