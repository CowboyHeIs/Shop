from django.db import models

class MoodEntry(models.Model):
    product = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.IntegerField()