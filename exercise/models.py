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
    GROUND_TYPES = (
        ('SAND', 'Sandy soil'),
        ('CLAY', 'Clay Soil'),
        ('SILT', 'Silt Soil'),
        ('PEAT', 'Peat Soil'),
        ('CHALK', 'Chalk Soil'),
        ('LOAM', 'Loam Soil')
    )
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    viable = models.BooleanField(default=models)
    groundType = models.CharField(max_length=5, choices=GROUND_TYPES)

    # an example function that if functional would return true if location is on land and thus can hav ea tree grow on it
    def is_viable(self):
        if self.longitude and self.latitude:  # assume that this is a function from a geolocation library that returns if location is viable
            return True
        else:
            return False

    def __str__(self):
        return self.get_rootType_display()


class Root(models.Model):
    ROOT_TYPE = (
        ('TAP', 'taproot'),
        ('FIB', 'fibrous'),
        ('ADV', 'adventitious')
    )
    groundLocation = models.ForeignKey(Ground, on_delete=models.CASCADE)
    rootType = models.CharField(max_length=3, choices=ROOT_TYPE)

    def __str__(self):
        return self.get_rootType_display()
