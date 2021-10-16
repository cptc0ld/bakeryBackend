from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from products.models import Products
from .renderer import JsonRenderer
from .serializers import OrderSerializer
from ..models import Order


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
@renderer_classes([JsonRenderer])
def create_order(request):
    if request.method == 'POST':
        data = {}
        try:
            header_token = request.headers['Authorization']
            token = Token.objects.get(key=header_token.split()[1])
            product = Products.objects.get(pk=request.data.get('productId'))
            order = Order.objects.create(product=product, user=token.user)
            order.save()
            serializers = OrderSerializer(order)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except:
            data['err'] = "Some error occurred"
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@renderer_classes([JsonRenderer])
def retrieve_order(request):
    if request.method == 'GET':
        data = {}
        try:
            header_token = request.headers['Authorization']
            token = Token.objects.get(key=header_token.split()[1])
            order = Order.objects.filter(user=token.user)
            serializers = OrderSerializer(order, many=True)
            data['order'] = serializers.data
            return Response(data, status=status.HTTP_200_OK)
        except:
            data['err'] = "Some error occurred"
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
