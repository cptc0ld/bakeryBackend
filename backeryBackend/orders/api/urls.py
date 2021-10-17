from django.urls import path

from orders.api.views import create_order, retrieve_order, retrieve_order_by_id

app_name = 'orders'

urlpatterns = [
    path('create', create_order, name="create_order"),
    path('get', retrieve_order, name="get_orders"),
    path('get/<int:id>', retrieve_order_by_id, name="get_order_by_id")
]
