from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from custom_auth.models import UserProfile
from .models import Equipe, Meta, AtualizarMeta
from .serializers import UserSerializer, UserUpdateSerializer, EquipeSerializer, EquipeUpdateSerializer, MetaSerializer, \
    MetaUpdateSerializer, AtualizarMetaSerializer


def index(request):
    context = {}
    return render(request, "home.html", context)


class UserProfileCreateView(generics.CreateAPIView):
    """
        API para criação de UserProfile
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super(UserProfileCreateView, self).create(request, *args, **kwargs)
            return response
        except Exception as e:
            print(request.data)
            print(f"Erro ao criar UserProfile: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

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

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super(EquipeCreateView, self).create(request, *args, **kwargs)


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

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super(MetaCreateView, self).create(request, *args, **kwargs)
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


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

    def update(self, request, *args, **kwargs):
        print(request.data)
        return super(MetaUpdateView, self).update(request, *args, **kwargs)


    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


class MetaRetrieveView(generics.RetrieveAPIView):
    """
        API para obter detalhes de uma Meta específica.
    """
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer



class AtualizacoesMetaListView(generics.ListAPIView):
    serializer_class = AtualizarMetaSerializer

    def get_queryset(self):
        """
        Este view deverá retornar uma lista de todas as atualizações
        para a meta conforme o id da meta passado na URL.
        """
        meta_id = self.kwargs['meta_id']
        return AtualizarMeta.objects.filter(meta_id=meta_id)



class AtualizarMetaCreateView(generics.CreateAPIView):
    queryset = AtualizarMeta.objects.all()
    serializer_class = AtualizarMetaSerializer

    def perform_create(self, serializer):
        meta = Meta.objects.get(pk=self.kwargs['meta_id'])
        serializer.save(meta=meta)
        meta.update_progress(serializer.validated_data['valorAtualizacao'])