from django.db import models

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2, default=39.99)

    def __str__(self):
        return self.title
