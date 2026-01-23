from django.db import models


class Cadastroclientes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=100)
    email = models.CharField(
        db_column='Email', unique=True, max_length=100, blank=True, null=True)
    senha = models.CharField(db_column='Senha', max_length=255)
    data_criação = models.DateTimeField(
        db_column='Data_criação', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadastroclientes'

    def __str__(self):
        return self.nome
