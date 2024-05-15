from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    def str(self):
        return self.name


class Yoqilgituri(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Zaprafka(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    lat = models.FloatField()
    lan = models.FloatField()
    description = models.TextField()
    closing_time = models.TimeField()
    opening_time = models.TimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    yoqilgituri = models.ForeignKey(Yoqilgituri, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='zaprafka/', blank=True, null=True)

    def str(self):
        return self.name
    
class Zaprafkacategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    zaprafka = models.ForeignKey(Zaprafka, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.name}, {self.zaprafka.name}'

