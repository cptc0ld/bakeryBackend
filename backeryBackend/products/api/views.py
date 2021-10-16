import json

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .renderer import JsonRenderer
from .serializers import ProductSerializer, IngredientSerializer, ProductRecipeSerializer
from ..models import Products, Ingredient, ProductsRecipe


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
@permission_classes([IsAuthenticated, ])
@renderer_classes([JsonRenderer])
def list_all_products_recipe(request, id):
    if request.method == 'GET':
        data = {}
        try:
            product = Products.objects.get(pk=id)
            product_recipe = ProductsRecipe.objects.get(pk=product)
            serializers = ProductRecipeSerializer(product_recipe)
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
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes([IsAdminUser, ])
@renderer_classes([JsonRenderer])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def update_product(request):
    if request.method == 'PUT':
        product_id = request.POST.get('id')
        product = Products.objects.get(pk=product_id)
        serializers = ProductSerializer(product, data=request.data)
        print(request.data)
        if serializers.is_valid():
            serializers.save()
            content = {'message': product.name + "Added"}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes([IsAdminUser, ])
@renderer_classes([JsonRenderer])
def delete_product(request, id):
    if request.method == 'DELETE':
        try:
            product = Products.objects.get(pk=id)
            name = product.name
            product.delete()
            content = {'message': name + " Deleted"}
            return Response(content, status=status.HTTP_200_OK)
        except:
            content = {'error_message': "some error"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
