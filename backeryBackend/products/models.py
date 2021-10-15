import json
import uuid
from django.db import models
from rest_framework import serializers


class MyIngredientsManager(models.Manager):
    pass


class Ingredients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    quantityPresent = models.IntegerField(default=0)
    costPrice = models.IntegerField(default=0)
    image = models.ImageField('Uploaded image', default='default.jpg')

    objects = MyIngredientsManager()

    def __str__(self):
        return self.name


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['name', 'quantityPresent', 'costPrice']


def set_ingredientsPresent(x):
    list_ing = []
    for ing in x:
        ingredient = Ingredients.objects.get(id=ing)
        list_ing.append(IngredientSerializer(ingredient).data)

    return list_ing


class MyProductManager(models.Manager):
    def create(self, data):
        item = self.model()
        item.name = data['name']
        item.ingredientsPresent = set_ingredientsPresent(data['ingredientsPresent'])
        return item


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    ingredientsPresent = models.JSONField(null=True)
    objects = MyProductManager()

    def __str__(self):
        return self.name
