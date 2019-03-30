from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    title           = models.CharField(max_length=100)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=10)
    quantity        = models.IntegerField(default=0, validators=[MaxValueValidator(50), MinValueValidator(0)])

    def __str__(self):
        return self.title
