from django.shortcuts import render
from rest_framework import generics
from .models import Gestor
from .serializers import GestorSerializer, GestorUpdateSerializer


def index(request):
    context = {}

    return render(request, "home.html", context)


class GestorCreateView(generics.CreateAPIView):
    """
        Api para criar de gestores
    """
    queryset = Gestor.objects.all()
    serializer_class = GestorSerializer


class GestorDeleteView(generics.DestroyAPIView):
    """
        Api para deletar de gestores
    """
    queryset = Gestor.objects.all()
    serializer_class = GestorSerializer


class GestorListView(generics.ListAPIView):
    """
        Api para listar de gestores
    """
    queryset = Gestor.objects.all()
    serializer_class = GestorSerializer


class GestorUpdateView(generics.UpdateAPIView):
    """
        Api para atualizar de gestores
    """
    queryset = Gestor.objects.all()
    serializer_class = GestorUpdateSerializer  # Use o novo serializer de atualização

    # Como email e senha são obrigatorios temos que fazer a altertação
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
