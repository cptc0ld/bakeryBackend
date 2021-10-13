import json

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import ProductSerializer, IngredientSerializer
from ..models import Products, Ingredients


@api_view(['GET', ])
@permission_classes([IsAdminUser, ])
def list_all_products(request):
    if request.method == 'GET':
        data = {}
        try:
            product = Products.objects.all()
            serializers = ProductSerializer(product, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            data['response'] = "Account does not exist"
        return Response(data)


@api_view(['POST', ])
@permission_classes([IsAdminUser, ])
def add_ingredients(request):
    if request.method == 'POST':
        data = ""
        ingredients = request.data.get('ingredients')
        data_ingredient = Ingredients.objects.create(ingredients)
        data_ingredient.save()
        serializers = IngredientSerializer(data_ingredient)
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes([IsAdminUser, ])
def add_products(request):
    if request.method == 'POST':
        products = request.data.get('products')
        data_products = Products.objects.create(products)
        data_products.save()
        serializers = ProductSerializer(data_products)
        return Response(serializers.data, status=status.HTTP_200_OK)
