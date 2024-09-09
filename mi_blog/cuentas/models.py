from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='usuarios',  # Nombre único para evitar conflictos
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios',  # Nombre único para evitar conflictos
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario',
    )

