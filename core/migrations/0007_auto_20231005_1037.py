# Generated by Django 3.2 on 2023-10-05 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20231005_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='colaboradores',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type_user': 3}, null=True, related_name='colaboradores_meta', to=settings.AUTH_USER_MODEL, verbose_name='Colaboradores'),
        ),
        migrations.AddField(
            model_name='meta',
            name='equipe',
            field=models.ManyToManyField(blank=True, null=True, related_name='equipes_meta', to='core.Equipe', verbose_name='Equipe'),
        ),
        migrations.AddField(
            model_name='meta',
            name='gestor',
            field=models.ForeignKey(blank=True, limit_choices_to={'type_user': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Gestor'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='colaboradores',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type_user': 3}, null=True, related_name='equipes', to=settings.AUTH_USER_MODEL, verbose_name='Colaboradores'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='gestor',
            field=models.ForeignKey(blank=True, limit_choices_to={'type_user': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Gestor'),
        ),
    ]