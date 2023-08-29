from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    count = models.PositiveIntegerField()
    discription = models.TextField(blank=True, null=True)
    visible = models.BooleanField(default=True)
