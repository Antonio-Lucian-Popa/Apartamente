from django.db import models

# Create your models here.

class Dobanda(models.Model):
    banca = models.CharField(max_length=100)
    dobanda = models.DecimalField(max_digits=5, decimal_places=2)
    data_actualizare = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.banca}: {self.dobanda}%"