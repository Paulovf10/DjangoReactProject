from django.shortcuts import render
from rest_framework import generics
from custom_auth.models import UserProfile
from .models import Equipe, Meta
from .serializers import UserSerializer, UserUpdateSerializer, EquipeSerializer, EquipeUpdateSerializer, MetaSerializer, \
    MetaUpdateSerializer


def index(request):
    context = {}
    return render(request, "home.html", context)


class UserProfileCreateView(generics.CreateAPIView):
    """
        API para criação de UserProfile
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserProfileDeleteView(generics.DestroyAPIView):
    """
        API para deletar UserProfile
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserProfileListView(generics.ListAPIView):
    """
        API para listar UserProfile
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserProfileUpdateView(generics.UpdateAPIView):
    """
        API para atualizar UserProfile
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserUpdateSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


class UserProfileRetrieveView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class EquipeCreateView(generics.CreateAPIView):
    """
        API para criação de Equipe.
    """
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class EquipeDeleteView(generics.DestroyAPIView):
    """
        API para deletar uma Equipe.
    """
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class EquipeListView(generics.ListAPIView):
    """
        API para listar Equipes.
    """
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class EquipeUpdateView(generics.UpdateAPIView):
    """
        API para atualizar uma Equipe.
    """
    queryset = Equipe.objects.all()
    serializer_class = EquipeUpdateSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


class EquipeRetrieveView(generics.RetrieveAPIView):
    """
        API para obter detalhes de uma Equipe específica.
    """
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class MetaCreateView(generics.CreateAPIView):
    """
        API para criação de Meta.
    """
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer


class MetaDeleteView(generics.DestroyAPIView):
    """
        API para deletar uma Meta.
    """
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer


class MetaListView(generics.ListAPIView):
    """
        API para listar Metas.
    """
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer


class MetaUpdateView(generics.UpdateAPIView):
    """
        API para atualizar uma Meta.
    """
    queryset = Meta.objects.all()
    serializer_class = MetaUpdateSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


class MetaRetrieveView(generics.RetrieveAPIView):
    """
        API para obter detalhes de uma Meta específica.
    """
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer
