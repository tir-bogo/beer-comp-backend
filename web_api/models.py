from django.db import models
from django.db.models import Count
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    image = models.CharField(max_length=1000, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.name}"

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])

        

