from django.urls import path

from .views import account_properties_view, ObtainAuthTokenView, registration_view, list_all_users

app_name = 'account'

urlpatterns = [
    path('properties', account_properties_view, name="properties"),
    path('login', ObtainAuthTokenView.as_view(), name="login"),
    path('register', registration_view, name="register"),
    path('all', list_all_users, name="all"),

]
