from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.api.urls', 'account_api')),
    path('api/product/', include('products.api.urls', 'products_api')),
    path('api/order/', include('orders.api.urls', 'orders_api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
