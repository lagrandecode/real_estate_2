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
    image = models.ImageField(null=True) 
    posted_time = models.CharField(auto_now_add=True)
    # image

    def __str__(self):
        return self.title