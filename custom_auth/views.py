import random
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import UserProfile
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

from .serializers import RegistrationSerializer, UserProfileSerializer


# USER API

class UserAPIView(APIView):
    def get(self, _):
        token = self.request.GET.get("token", "")
        user_token = get_object_or_404(Token, key=token)

        serializer = UserProfileSerializer(user_token.user)

        return Response(serializer.data)


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



