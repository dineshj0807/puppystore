from rest_framework import serializers
from puppy.models import Puppy

class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = '__all__'