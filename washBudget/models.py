from django.db import models

# Create your models here.
class Sofa(models.Model):
    num_pessoas = models.IntegerField()
    modelosofa = models.CharField(max_length=50)
    materialsofa = models.CharField(max_length=50)
    servicosofa = models.CharField(max_length=50) 