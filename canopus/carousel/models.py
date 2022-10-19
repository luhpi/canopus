from enum import unique
from tkinter import CASCADE
from django.db import models
from user.models import User

class Carousel(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    # add more info to each carousel if needed
    

class Image(models.Model):
    carousel = models.ForeignKey(Carousel,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery')
