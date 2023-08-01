from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    weight = models.IntegerField()
    diet = models.TextField(max_length=250)
    vaccinated = models.BooleanField(default=True)

    def __str__(self):
        return self.name