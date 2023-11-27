from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()