from django.db import models

# Create your models here.

class Puppy(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    breed = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str(self)

    def get_breed(self):
        return self.name + ' belongs to ' + self.breed + ' breed'