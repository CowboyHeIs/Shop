from django.db import models

class Product(models.Model):
    product = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.IntegerField()

    def __str__(self) :
        return self.product