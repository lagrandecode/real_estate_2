from difflib import SequenceMatcher
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bed = models.IntegerField()
    num_bath = models.IntegerField()
    Sqare = models.IntegerField()
    address = models.CharField(max_length=500)
    # image

    def __str__(self):
        return self.title