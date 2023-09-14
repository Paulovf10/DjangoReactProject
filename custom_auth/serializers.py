from rest_framework import serializers
from .models import UserProfile, UserAddress
from django.db import transaction


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = (
            'user', 'name', 'postal_code', 'address', 'address_neighborhood', 'address_number', 'address_complement',
            'city', 'state', 'is_principal', 'id',)


class UserProfileSerializer(serializers.ModelSerializer):
    user_address = UserAddressSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'unique_id', 'name', 'identifier', 'email', 'birth_date', 'phone', 'cpf', 'is_premium',
            'is_superuser', 'is_staff', 'is_active', 'last_login', 'date_joined', 'user_address', 'device_id')


class RegistrationSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y'])

    class Meta:
        model = UserProfile
        fields = ['name', 'cpf', 'email', 'phone', 'birth_date', 'password', 'device_id']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = UserProfile(
            name=self.validated_data['name'],
            cpf=self.validated_data['cpf'],
            email=self.validated_data['email'],
            identifier=self.validated_data['email'],
            phone=self.validated_data['phone'],
            birth_date=self.validated_data['birth_date'],
        )
        with transaction.atomic():
            password = self.validated_data['password']
            user.set_password(password)
            user.save()
            print(user)

        return user
