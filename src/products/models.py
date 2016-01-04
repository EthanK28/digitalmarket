from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=140)  # sdlfldsfjaslk
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=6.99, blank=True, null=True)


    def __str__(self):
        return self.title

