from django.db import models


class Ingredient(models.Model):
    id = models.SlugField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    costPrice = models.IntegerField(default=0)
    image = models.ImageField('Uploaded image', default='default.jpg')


class Products(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class IngredientsPresent(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.ingredient.name


class ProductsRecipe(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE, primary_key=True)
    ingredients = models.ManyToManyField(IngredientsPresent)

    def __str__(self):
        return self.product.name
