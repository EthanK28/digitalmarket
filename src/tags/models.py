from django.db import models

# Create your models here.
from products.models import (
    Product
)

class Tag(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    products = models.ManyToManyField(Product, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

