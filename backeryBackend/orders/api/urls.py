from django.urls import path

from orders.api.views import create_order, retrieve_order

app_name = 'orders'

urlpatterns = [
    path('create', create_order, name="create_order"),
    path('get', retrieve_order, name="get_orders")
]
