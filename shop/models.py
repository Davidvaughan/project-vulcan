from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default=None, null=True)
    display = models.BooleanField(null=True)

    def __str__(self):

        return self.name


class Product(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=3000, default=None, null=True)
    countryOrigin = models.CharField(max_length=100, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):

        return self.name
