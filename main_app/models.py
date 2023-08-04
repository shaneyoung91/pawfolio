from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Treat(models.Model):
    name = models.CharField(max_length=50)
    flavor = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        permissions = [
            ("create_treat", "Can create treat"),
            ("remove_treat", "Can delete treat"),
        ]

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    weight = models.IntegerField()
    diet = models.TextField(max_length=250)
    vaccinated = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    treats = models.ManyToManyField(Treat)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
    
GRADES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('F', 'F'),
)

class ReportCard(models.Model):
    date = models.DateField()
    behavior = models.TextField(max_length=250)
    summary = models.TextField(max_length=250)
    grade = models.CharField(
        max_length=1,
        choices=GRADES,
        default=GRADES[0][0]
    )
    fed = models.BooleanField(default=True)
    photo_url = models.URLField(blank=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_grade_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    reportcard = models.ForeignKey(ReportCard, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Photo for dog_id: {self.dog_id} @{self.url}'