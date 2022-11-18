'''
from django.test import TestCase
from puppy.models import Puppy

class PuppyModelTest(TestCase):
    """Test Module for puppy model"""
    def setUp(self):
        Puppy.objects.create(name = 'casper', age = 2, breed = 'beagle')
        Puppy.objects.create(name = 'rocky', age = 1, breed = 'dalmatian')
        Puppy.objects.create(name = 'muffin', age = 2, breed = 'pug')

    def test_get(self):
        casper = Puppy.objects.get(name = 'casper')
        rocky = Puppy.objects.get(name = 'rocky')
        muffin = Puppy.objects.get(name = 'muffin')
        self.assertEqual(casper.breed, "beagle")
        self.assertEqual(rocky.breed, "dalmatian")
        self.assertEqual(muffin.breed, "pug")

    def test_create(self):
        moti = Puppy.objects.create(name = 'moti', age = 3, breed = 'Native Indian')
        # self.assertEqual(moti.breed, 'Native Indian')
        self.assertTrue(isinstance(moti, Puppy))


    def test_update(self):
        casper = Puppy.objects.get(name = 'casper')
        casper.breed = 'German Sheferd'
        casper.save()
        self.assertEqual(casper.breed, "German Sheferd")

    def test_delete(self):
        casper = Puppy.objects.get(name = 'casper')
        casper.delete()
        self.assertTrue(casper.DoesNotExist())

'''
    