import json

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .renderer import JsonRenderer
from .serializers import ProductSerializer, IngredientSerializer, ProductRecipeSerializer
from ..models import Products, Ingredient


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@renderer_classes([JsonRenderer])
def list_all_products(request):
    if request.method == 'GET':
        data = {}
        try:
            product = Products.objects.all()
            serializers = ProductSerializer(product, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except:
            data['err'] = "Some error occurred"
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', ])
@permission_classes([IsAdminUser, ])
@renderer_classes([JsonRenderer])
def list_all_ingredients(request):
    if request.method == 'GET':
        data = {}
        try:
            ingredients = Ingredient.objects.all()
            serializers = IngredientSerializer(ingredients, many=True)
            content = {'ingredients': serializers.data}
            return Response(content, status=status.HTTP_200_OK)
        except:
            data['err'] = "Some error occurred"
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', ])
@permission_classes([IsAdminUser, ])
@renderer_classes([JsonRenderer])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def add_ingredients(request):
    if request.method == 'POST':
        serializers = IngredientSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            content = {'added': serializers.data}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes([IsAdminUser, ])
@renderer_classes([JsonRenderer])
def add_products(request):
    if request.method == 'POST':
        serializers = ProductRecipeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            content = {'message': request.data.get('product')['name'] + "Added"}
            return Response(content, status=status.HTTP_200_OK)
        else:
            print(serializers.data)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
