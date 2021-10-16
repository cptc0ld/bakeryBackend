from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data, **kwargs):
        product = kwargs.get('product')
        user = kwargs.get('user')
        ingredient_present_model = Order.objects.create(product=product, user=user)
        return ingredient_present_model
