from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
import uuid

from core.choices import TIPO_USUARIO


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, identifier, name, password=None):
        """Creates a new user profile."""

        if not identifier:
            raise ValueError('Usuários precisam de um identificador')

        # email = self.normalize_email(email)
        user = self.model(identifier=identifier, name=name, )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, identifier, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(identifier, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser):
    """
    Represents a "user profile" inside out system. Stores all user account
    related data, such as 'email address' and 'name'.
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True, )
    identifier = models.CharField(max_length=80, verbose_name='Identificador', unique=True)

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, )
    birth_date = models.DateField(verbose_name='Data de nascimento', null=True, blank=True, )
    phone = models.CharField(max_length=30, verbose_name='Telefone', null=True, blank=True, )

    is_staff = models.BooleanField(default=False, verbose_name='Staff')

    cpf = models.CharField(max_length=30, verbose_name='CPF', null=True, blank=True, )
    addres = models.CharField(max_length=100, verbose_name='Endereço', null=True, blank=True, )
    type_user = models.SmallIntegerField(verbose_name='Tipo de usuário', null=True, blank=True, choices=TIPO_USUARIO)
    profile_picture = models.FileField(verbose_name="Foto de perfil", null=True, blank=True, upload_to="perfil")

    objects = UserProfileManager()

    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['name']

    @property
    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, perm, obj=None):
        return True

    def get_short_name(self):
        """Django uses this when it needs to get the users abbreviated name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.name

    class Meta:
        verbose_name = u"Usuário"
        verbose_name_plural = u"Usuários"
        ordering = ('name',)
