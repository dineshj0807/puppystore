import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer


# initialize the APIClient app
client = Client()


class PuppiesApiTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        self.casper = Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog')
        self.muffin = Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane')
        self.rambo = Puppy.objects.create(
            name='Rambo', age=2, breed='Labrador')
        self.ricky = Puppy.objects.create(
            name='Ricky', age=6, breed='Labrador')

        self.valid_payload = {
            'name': 'xyz',
            'age': 10,
            'breed': 'unknown',
        }
        self.nvalid_payload = {
            'name': 'ponting',
            'age': 6,
            'breed': 'Labrador',
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
        }

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_puppies'))
        # get data from db
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_puppy(self):
        response = client.post(reverse('get_post_puppies'), data=json.dumps(
            self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(reverse('get_post_puppies'), data=json.dumps(
            self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_puppy(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}))

        puppy = Puppy.objects.get(pk=self.muffin.pk)
        ser = PuppySerializer(puppy)
        self.assertEqual(response.data, ser.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_puppy', kwargs={'pk': self.rambo.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        response = client.put(reverse('get_delete_update_puppy', kwargs={
                              'pk': self.muffin.pk}), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
