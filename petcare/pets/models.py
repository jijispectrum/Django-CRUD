from django.db import models

# Create your models here.
from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    owner_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.species})'
