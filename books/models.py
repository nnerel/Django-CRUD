from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='author')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    pages = models.DecimalField(max_digits=4, decimal_places=0)
    premiere = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s | %s" % (self.title, self.author)

    def get_absolute_url(self):
        return reverse("books:book_list")
