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


class Ground(models.Model):
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    viable = models.BooleanField(default=models)

    # an example function that if functional would return true if location is on land and thus can hav ea tree grow on it
    def is_viable(self):
        if self.longitude and self.latitude:  # assume that this is a function from a geolocation library that returns if location is viable
            return True
        else:
            return False

    def __str__(self):
        return self
