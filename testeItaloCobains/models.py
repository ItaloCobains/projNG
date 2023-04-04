from django.db import models

# Create your models here.

class Sofa(models.Model):
    num_pessoas = models.IntegerField()
    modelo = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    servicos = models.CharField(max_length=100)


    def __str__(self):
        return self.modelo

