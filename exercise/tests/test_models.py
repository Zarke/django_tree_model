from django.test import TestCase
from ..models import Ground


# Create your tests here.
class GroundModelTest(TestCase):
    soil = Ground(longitude=2, latitude=5, )

    def test_verbose_plural(self):
        self.assertEqual(Ground._meta.verbose_name_plural, "Soil types")

    def test_is_viable(self, soil=soil):
        first_quadrant = True
        if soil.longitude < 0 or soil.latitude < 0:
            first_quadrant = False

        self.assertTrue(first_quadrant, "Soil is not viable")

    def test_string_representation(self, soil=soil):
        GROUND_TYPES = (
            ('SAND', 'Sandy soil'),
            ('CLAY', 'Clay Soil'),
            ('SILT', 'Silt Soil'),
            ('PEAT', 'Peat Soil'),
            ('CHALK', 'Chalk Soil'),
            ('LOAM', 'Loam Soil')
        )
        self.assertEqual(str(soil.groundType), GROUND_TYPES[0][0])
