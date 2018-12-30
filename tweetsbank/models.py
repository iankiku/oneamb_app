from django.db import models

# Create your models here.
class tweets(models.Model):
    text = models.TextField()