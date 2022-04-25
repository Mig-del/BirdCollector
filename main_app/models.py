from django.db import models

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=100)
    specie = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()


    def __str__(self):
        return f"The bird named {self.name} has id of {self.id}"