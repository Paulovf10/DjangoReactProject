from custom_auth.models import UserProfile
from rest_framework import serializers
from .models import Equipe, Meta, AtualizarMeta, Relatorio

"""
    Transforma o json em objetos python, foi utilizada funções genericas na criação.
"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'


class EquipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'
        read_only_fields = ('gestor',)  # Supondo que você não queira que o gestor seja modificado após a criação


class MetaSerializer(serializers.ModelSerializer):
    """
    Serializer padrão para o modelo Meta.
    """
    gestor = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.filter(type_user=2))
    colaboradores = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.filter(type_user=3))
    equipe = serializers.PrimaryKeyRelatedField(many=True, queryset=Equipe.objects.all())

    class Meta:
        model = Meta
        fields = '__all__'


class AtualizarMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtualizarMeta
        fields = ['id', 'comentario', 'valorAtualizacao', 'criadoEm']


class MetaUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para atualização do modelo Meta.
    Permite atualizações parciais.
    """
    atualizacoes = AtualizarMetaSerializer(many=True, read_only=True)

    class Meta:
        model = Meta
        fields = '__all__'


class RAtualizarMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtualizarMeta
        fields = ['comentario', 'valorAtualizacao', 'criadoEm']

class RMetaSerializer(serializers.ModelSerializer):
    atualizacoes = RAtualizarMetaSerializer(many=True, read_only=True)

    class Meta:
        model = Meta
        fields = ['nome', 'descricao', 'tipoMeta', 'valorAlvo', 'progressoAtual',
                  'unidadeMedida', 'dataInicio', 'dataFim', 'metaBatida', 'ativo', 'atualizacoes']
class RelatorioSerializer(serializers.Serializer):
    tipo = serializers.ChoiceField(choices=['colaborador', 'equipe'])
    id = serializers.IntegerField()
    metas = RMetaSerializer(many=True, read_only=True)
