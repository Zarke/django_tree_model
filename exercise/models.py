from django.db import models


# Create your models here.

class Tree(models.Model):
    CLIMATE = (
        ('TRO', 'Tropical'),
        ('DES', 'Desert'),
        ('ARC', 'Arctic'),
        ('RFR', 'Rainforest'),
        ('MOD', 'Moderate')
    )

    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=3, choices=CLIMATE, default='MOD')

    def __str__(self):
        return self.name
