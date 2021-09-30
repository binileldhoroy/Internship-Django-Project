from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Location(models.Model):
    district = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.district} ({self.address})'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Interns(models.Model):
    title = models.CharField(max_length=200)
    organizoremail = models.EmailField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    seat = models.IntegerField()
    date = models.DateField()
    host = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participant = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return self.title 

    