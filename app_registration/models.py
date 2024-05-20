from django.db import models

class Cars(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    ano = models.IntegerField()
