from django.utils.text import slugify
from rest_framework import serializers
from ..models import Products, Ingredient, ProductsRecipe, IngredientsPresent


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ['id']

    def to_representation(self, instance):
        data = super(IngredientSerializer, self).to_representation(instance)
        data['image'] = " http://127.0.0.1:8000" + data['image']
        return data

    def create(self, validated_data):
        name = validated_data.pop('name')
        ingredient = {
            'id': slugify(name),
            'name': name,
            'costPrice': validated_data.pop('costPrice'),
            'image': validated_data.pop('image'),
            'quantity': validated_data.pop('quantity')
        }
        ingredient_model = Ingredient.objects.create(**ingredient)
        return ingredient_model


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        data['image'] = " http://127.0.0.1:8000" + data['image']
        return data


class IngredientsPresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsPresent
        fields = ['ingredient', 'quantity']

    def create(self, validated_data, **kwargs):
        product = kwargs.get('product')
        ingredient = validated_data.pop('ingredient')
        quantity = validated_data.pop('quantity')
        ingredient_model = Ingredient.objects.get(id=ingredient)
        ingredient_present_model = IngredientsPresent.objects.create(ingredient=ingredient_model, quantity=quantity,
                                                                     product=product)

        return ingredient_present_model


class ProductRecipeSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    ingredients = IngredientsPresentSerializer(many=True)

    class Meta:
        model = ProductsRecipe
        fields = ['product', 'ingredients']

    def create(self, validated_data):
        product = validated_data.pop('product')
        product_model = Products.objects.create(**product)
        product_recipe = ProductsRecipe.objects.create(product=product_model)
        ingredients = validated_data.pop('ingredients')
        for i in ingredients:
            ingredients_model = IngredientsPresent.objects.create(product=product_model, **i)
            product_recipe.ingredients.add(ingredients_model)

        return product_recipe
