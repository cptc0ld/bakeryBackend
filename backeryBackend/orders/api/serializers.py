from rest_framework import serializers

from orders.models import Order
from products.api.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'orderDate', 'product', 'user']

    def create(self, validated_data, **kwargs):
        product = kwargs.get('product')
        user = kwargs.get('user')
        ingredient_present_model = Order.objects.create(product=product, user=user)
        return ingredient_present_model
