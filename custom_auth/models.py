from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
import uuid


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


class UserProfile(AbstractBaseUser, PermissionsMixin):
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

    cpf = models.CharField(max_length=30, verbose_name='CPF', null=True, blank=True, )

    is_premium = models.BooleanField(verbose_name='Assinatura ativa?', default=False)
    device_id = models.CharField(max_length=50, verbose_name='Device ID', null=True, blank=True, default=None)

    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')

    objects = UserProfileManager()

    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['name']

    @property
    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return self.name

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


class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='Usuário', on_delete=models.PROTECT, related_name='user_address')
    name = models.CharField(max_length=200, verbose_name='Identificação do endereço', null=True, blank=True, )
    postal_code = models.CharField(max_length=12, verbose_name='CEP', null=True, blank=True, )
    address = models.CharField(max_length=200, verbose_name=u'Endereço', null=True, blank=True, )
    address_neighborhood = models.CharField(max_length=50, verbose_name=u'Bairro', null=True, blank=True, )
    address_number = models.CharField(max_length=50, verbose_name=u'Número', null=True, blank=True, )
    address_complement = models.CharField(max_length=50, verbose_name=u'Complemento', null=True, blank=True, )
    city = models.CharField(max_length=40, verbose_name='Cidade', null=True, blank=True, )
    state = models.CharField(max_length=2, verbose_name='Estado', null=True, blank=True, )
    is_principal = models.BooleanField(verbose_name='Endereço principal?', default=False)

    def str(self):
        return self.name or u''

    class Meta:
        verbose_name = u'Usuário - Endereço'
        verbose_name_plural = u'Usuários - Endereços'
