import inspect
import os

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .renderer import JsonRenderer
from .serializers import RegistrationSerializer, AccountPropertiesSerializer
from ..models import Account



@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
@renderer_classes([JsonRenderer])
def registration_view(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) is not None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username', '0')
        if validate_username(username) is not None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['pk'] = account.pk
            token = Token.objects.get(user=account).key
            data['token'] = token
            data['is_admin'] = account.is_admin
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def validate_email(email):
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account != None:
        return email


def validate_username(username):
    account = None
    try:
        account = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None
    if account != None:
        return username


# Account properties
# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
@renderer_classes([JsonRenderer])
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)


# LOGIN
# URL: http://127.0.0.1:8000/api/account/login
class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []
    renderer_classes = [JsonRenderer]

    def post(self, request):
        context = {}

        email = request.data.get('email')
        password = request.data.get('password')
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['email'] = email.lower()
            context['token'] = token.key
            context['is_admin'] = account.is_admin
            context['username'] = account.username
            return Response(context, status=status.HTTP_200_OK)
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
@renderer_classes([JsonRenderer])
def does_account_exist_view(request):
    if request.method == 'GET':
        email = request.GET['email'].lower()
        data = {}
        try:
            account = Account.objects.get(email=email)
            data['response'] = email
        except Account.DoesNotExist:
            data['response'] = "Account does not exist"
        return Response(data)


@api_view(['GET', ])
@permission_classes([IsAdminUser, ])
@renderer_classes([JsonRenderer])
def list_all_users(request):
    if request.method == 'GET':
        data = {}
        try:
            account = Account.objects.all()
            serializers = AccountPropertiesSerializer(account, many=True)
            content = {'users': serializers.data}
            return Response(content, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            data['response'] = "Account does not exist"
        return Response(data)
