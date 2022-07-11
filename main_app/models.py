from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    photo = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={finch_id: self.id})
