from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response

from custom_auth.models import UserProfile
from .constants import EnumTipoUsuario
from .models import Equipe, Meta, AtualizarMeta, Relatorio
from .serializers import UserSerializer, UserUpdateSerializer, EquipeSerializer, EquipeUpdateSerializer, MetaSerializer, \
    MetaUpdateSerializer, AtualizarMetaSerializer, RelatorioSerializer, RMetaSerializer, LoginSerializer, \
    RelatorioSerializerV


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


class RelatorioAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        relatorio_serializer = RelatorioSerializer(data=request.data)
        relatorio_serializer.is_valid(raise_exception=True)

        tipo = relatorio_serializer.validated_data['tipo']
        id = relatorio_serializer.validated_data['id']

        if tipo == 'colaborador':
            entity = UserProfile.objects.filter(type_user=3, id=id).first()
            if not entity:
                return Response({'error': 'Colaborador não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
            metas = Meta.objects.filter(colaboradores=entity)
        elif tipo == 'equipe':
            entity = Equipe.objects.filter(id=id).first()
            if not entity:
                return Response({'error': 'Equipe não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
            metas = Meta.objects.filter(equipe=entity)
        else:
            return Response({'error': 'Tipo inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        # Calculando os scores
        hoje = timezone.now().date()
        quantidade = metas.count()
        finalizadas = metas.filter(metaBatida=True).count()
        emAberto = metas.filter(dataFim__gte=hoje, metaBatida=False).count()
        naoFinalizadas = metas.filter(dataFim__lt=hoje, metaBatida=False).count()
        taxaSucesso = finalizadas / quantidade * 100 if quantidade else 0

        # Atribuindo uma nota baseada na taxa de sucesso (exemplo simplificado)
        if taxaSucesso >= 90:
            notaFinal = ('S', 1)
        elif taxaSucesso >= 80:
            notaFinal = ('A', 2)
        elif taxaSucesso >= 70:
            notaFinal = ('B', 3)
        elif taxaSucesso >= 60:
            notaFinal = ('C', 4)
        elif taxaSucesso >= 50:
            notaFinal = ('D', 5)
        else:
            notaFinal = ('F', 6)

        # Criando o relatório
        relatorio = Relatorio.objects.create(
            tipoRelatorio=1 if tipo == 'colaborador' else 2,
            colaborador=entity if tipo == 'colaborador' else None,
            equipe=entity if tipo == 'equipe' else None,
            quantidade=quantidade,
            finalizadas=finalizadas,
            emAberto=emAberto,
            naoFinalizadas=naoFinalizadas,
            taxaSucesso=taxaSucesso,
            notaFinal=notaFinal[1]
        )

        # Serializando o relatório
        metas_serializer = RMetaSerializer(metas, many=True)
        relatorio_data = {
            'tipo': tipo,
            'id': id,
            'quantidade': quantidade,
            'finalizadas': finalizadas,
            'emAberto': emAberto,
            'naoFinalizadas': naoFinalizadas,
            'taxaSucesso': taxaSucesso,
            'notaFinal': notaFinal[0],
            'metas': metas_serializer.data
        }
        return Response(relatorio_data)


class RelatorioListView(generics.ListAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializerV


class RelatorioDetailView(generics.RetrieveAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

    def retrieve(self, request, *args, **kwargs):
        relatorio = self.get_object()

        # Suponha que 'metas' é um campo de relacionamento reverso de Relatorio para Meta

        tipo = relatorio.tipoRelatorio
        id = relatorio
        print(tipo)
        if tipo == 1:
            id = relatorio.colaborador.id
            entity = UserProfile.objects.filter(type_user=3, id=id).first()
            metas = Meta.objects.filter(colaboradores=entity)
        elif tipo == 2:
            id = relatorio.equipe.id
            entity = Equipe.objects.filter(id=id).first()
            metas = Meta.objects.filter(equipe=entity)

        hoje = timezone.now().date()
        quantidade = metas.count()
        finalizadas = metas.filter(metaBatida=True).count()
        emAberto = metas.filter(dataFim__gte=hoje, metaBatida=False).count()
        naoFinalizadas = metas.filter(dataFim__lt=hoje, metaBatida=False).count()
        taxaSucesso = finalizadas / quantidade * 100 if quantidade else 0

        notaFinal = ('S' if taxaSucesso >= 90 else
                     'A' if taxaSucesso >= 80 else
                     'B' if taxaSucesso >= 70 else
                     'C' if taxaSucesso >= 60 else
                     'D' if taxaSucesso >= 50 else
                     'F')

        metas_serializer = RMetaSerializer(metas, many=True)
        relatorio_data = {
            'tipo': 'colaborador' if relatorio.colaborador else 'equipe',
            'id': relatorio.id,
            'quantidade': quantidade,
            'finalizadas': finalizadas,
            'emAberto': emAberto,
            'naoFinalizadas': naoFinalizadas,
            'taxaSucesso': taxaSucesso,
            'notaFinal': notaFinal,
            'metas': metas_serializer.data
        }
        print(relatorio_data)
        return Response(relatorio_data)


class RelatorioDeleteView(generics.DestroyAPIView):
    """
        API para deletar relatorio
    """
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializerV


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        queryset = UserProfile.objects.filter().exclude(type_user=EnumTipoUsuario.ADMINISTRADOR.value)
        try:
            user = queryset.get(email=request.data['email'], password=request.data['senha'])
            return Response({'message': 'Login Successful', "tipo": f"{user.type_user}", "name": user.name},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
