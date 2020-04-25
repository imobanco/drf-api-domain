# Generated by Django 3.0.5 on 2020-04-25 19:16

import core.models
from django.db import migrations, models
import users.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='email do usuário', max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(help_text='senha do usuário', max_length=128, verbose_name='senha')),
                ('_picture', models.ImageField(blank=True, help_text='imagem de perfil', null=True, upload_to=users.utils.picture_path, verbose_name='imagem de perfil')),
                ('is_staff', models.BooleanField(default=False, help_text='usuário tem acesso à interface admin?', verbose_name='staff status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['email'],
            },
            bases=(models.Model, core.models.UserOwnerMixin),
        ),
    ]
