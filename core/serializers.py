from rest_framework import serializers
from .models import Gestor

"""
    Transforma o json em objetos python, foi utilizada funções genericas na criação.
"""
class GestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = '__all__'


class GestorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = '__all__'