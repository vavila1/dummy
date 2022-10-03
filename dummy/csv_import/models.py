from django.db import models

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + '-' + self.matricula
