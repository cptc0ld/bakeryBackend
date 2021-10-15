import json

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .renderer import JsonRenderer
from .serializers import ProductSerializer, IngredientSerializer
from ..models import Products, Ingredients


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
            ingredients = Ingredients.objects.all()
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
        print(request.data)
        # data_ingredient = Ingredients.objects.create(ingredients)
        # data_ingredient.save()
        serializers = IngredientSerializer(data=request.data)
        # import pdb; pdb.set_trace()
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
        products = request.data.get('products')
        try:
            data_products = Products.objects.create(products)
            data_products.save()
            content = {'message': products["name"] + " Added"}
            return Response(content, status=status.HTTP_200_OK)
        except:
            content = {'error_message': products["name"] + " Already Exist"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
