# -*- coding: utf-8 -*-
from django.db import models


class Usuarios(models.Model):
    nome_usuario = models.CharField(unique=True, max_length=50)
    senha_hash = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'usuarios'
