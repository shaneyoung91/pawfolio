from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    weight = models.IntegerField()
    diet = models.TextField(max_length=250)
    vaccinated = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})