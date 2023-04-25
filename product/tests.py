from django.test import TestCase
from product.models import Product


class PuppyTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Product.objects.create(
            title='Casper', price=3, description='Bull Dog')
        Product.objects.create(
            title='Muffin', price=1, description='Gradane')

    def test_puppy_breed(self):
        puppy_casper = Product.objects.get(title='Casper')
        puppy_muffin = Product.objects.get(title='Muffin')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
        self.assertEqual(
            puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")