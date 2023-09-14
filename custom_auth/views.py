import random
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import UserProfile, UserAddress
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

from .serializers import RegistrationSerializer, UserProfileSerializer, UserAddressSerializer


# USER API

class UserAPIView(APIView):
    def get(self, _):
        token = self.request.GET.get("token", "")
        user_token = get_object_or_404(Token, key=token)

        serializer = UserProfileSerializer(user_token.user)

        return Response(serializer.data)


@api_view(["POST"])
@permission_classes((AllowAny,))
def registration_view(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data['message'] = "Cadastro realizado com sucesso! "
            data['identifier'] = user.identifier
            token_obj, created = Token.objects.get_or_create(user=user)

            postal_code = request.data.get("postal_code")
            address = request.data.get("address")
            address_number = request.data.get("address_number")
            address_complement = request.data.get("address_complement")
            address_neighborhood = request.data.get("address_neighborhood")
            city = request.data.get("city")
            state = request.data.get("state")
            UserAddress.objects.create(user=user, postal_code=postal_code, address=address, is_principal=True,
                                       address_number=address_number, address_complement=address_complement,
                                       address_neighborhood=address_neighborhood, city=city, state=state)

            token = token_obj.key
            data['token'] = token
        else:
            data = serializer.errors

    print(data)
    return Response(data)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
    username = request.data.get("identifier")
    password = request.data.get("password")
    device_id = request.data.get("device_id")

    if username is None or password is None:
        return Response({'error': 'Todos os campos são obrigatórios'}, status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'E-mail ou senha não conferem. Tente novamente.'}, status=HTTP_404_NOT_FOUND)

    identifier = user.identifier
    token, created = Token.objects.get_or_create(user=user)

    if user and device_id:
        user.device_id = device_id
        user.save()

    return Response({'token': token.key, "identifier": identifier}, status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes((AllowAny,))
def check_user_view(request):
    if request.user.is_authenticated:
        if request.user.is_premium:
            return Response({"is_premium": True})
    return Response({"is_premium": False})


@api_view(["POST"])
@permission_classes((AllowAny,))
def change_user_password(request):
    old_password = request.data.get("old_password")
    new_password = request.data.get("new_password")
    confirm_new_password = request.data.get("confirm_new_password")
    user_token = request.data.get("token")

    if not old_password or not new_password or not user_token or not confirm_new_password:
        return Response({'error': 'Todos os campos são obrigatórios'}, status=HTTP_400_BAD_REQUEST)

    if new_password != confirm_new_password:
        return Response({'error': 'Confirmação de senha não confere'}, status=HTTP_400_BAD_REQUEST)

    token_obj = get_object_or_404(Token, key=user_token)
    current_user = token_obj.user

    authentication = authenticate(username=current_user.identifier, password=old_password)

    if authentication:
        current_user.set_password(new_password)
        current_user.save()
        return Response({}, status=HTTP_200_OK)
    else:
        return Response({'error': 'Informações incorretas, confira os dados e tente novamente.'},
                        status=HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((AllowAny,))
def save_address(request):
    user_token = request.data.get("token")

    token_obj = get_object_or_404(Token, key=user_token)
    user = token_obj.user

    name = request.data.get("name", "")
    postal_code = request.data.get("postal_code", "").replace("-", "").replace(".", "")
    address = request.data.get("address", "")
    address_neighborhood = request.data.get("address_neighborhood", "")
    address_number = request.data.get("address_number", "")
    address_complement = request.data.get("address_complement", "")
    city = request.data.get("city", "")
    state = request.data.get("state", "")

    user_address, created = UserAddress.objects.get_or_create(user=user, name=name, postal_code=postal_code,
                                                              address=address, is_principal=True,
                                                              address_neighborhood=address_neighborhood,
                                                              address_number=address_number,
                                                              address_complement=address_complement, city=city,
                                                              state=state)
    if created:
        return Response({}, status=HTTP_200_OK)
    else:
        return Response({'error': 'Registro duplicado.'}, status=HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def set_principal_address(request):
    user = request.user

    address_id = request.data.get("address_id", "")
    address = get_object_or_404(UserAddress, pk=address_id)

    if address.user == user:
        UserAddress.objects.filter(user=user).update(is_principal=False)

        address.is_principal = True
        address.save()

        return Response({}, status=HTTP_200_OK)

    else:
        return Response({'error': 'Operação inválida.'}, status=HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_principal_address(request):
    user = request.user

    address = UserAddress.objects.filter(is_principal=True, user=user).first()
    address_serializer = UserAddressSerializer(address)

    return Response(address_serializer.data, status=HTTP_200_OK)
