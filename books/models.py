from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='author')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    pages = models.DecimalField(max_digits=4, decimal_places=0)
    premiere = models.DateField(null=True, blank=True)
