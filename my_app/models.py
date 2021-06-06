from django.db import models

# Create your models here.
class Predictions(models.Model):

    image = models.CharField(max_length = 150)
    prediction = models.IntegerField()

