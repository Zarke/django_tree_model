from django.db import models


# Create your models here.
class Ground(models.Model):
    GROUND_TYPES = (
        ('SAND', 'Sandy soil'),
        ('CLAY', 'Clay Soil'),
        ('SILT', 'Silt Soil'),
        ('PEAT', 'Peat Soil'),
        ('CHALK', 'Chalk Soil'),
        ('LOAM', 'Loam Soil')
    )
    longitude = models.IntegerField(default=0, blank=False)
    latitude = models.IntegerField(default=0, blank=False)
    viable = models.BooleanField(default=True)
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


class Trunk(models.Model):
    diameter = models.IntegerField(default=None, blank=True)
    age = models.IntegerField(default=None, blank=True)
    attachedRoot = models.ForeignKey(Root, on_delete=models.CASCADE)


class Branch(models.Model):
    length = models.IntegerField(default=None, blank=True)
    width = models.IntegerField(default=None, blank=True)
    is_healty = models.BooleanField(default=True)
    attached_trunk = models.ForeignKey(Trunk, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_healty:
            return f'This is a healty {self.width}cm long branch'
        else:
            return f'This is a damaged {self.width} branch'


class Leaf(models.Model):
    LEAF_TYPES = (
        ('ALT', 'Alternate'),
        ('OPO', 'Opposite'),
        ('WHO', 'Whorled'),
        ('BAC', 'Basal')
    )

    leaf_type = models.CharField(max_length=3, choices=LEAF_TYPES)
    surface = models.IntegerField(default=None, blank=True)
    attached_to_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


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
    connected_trunk = models.OneToOneField(Trunk, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
