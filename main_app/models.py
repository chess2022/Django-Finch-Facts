from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
SIGHTINGS = (
    ('S', 'Physically Seen'),
    ('H', 'Heard Song')
)

class Finch(models.Model):
    photo = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Sighting(models.Model):
    date = models.DateField('sighting date')
    type = models.CharField(
        max_length=1,
        choices=SIGHTINGS,
        default=SIGHTINGS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_sighting_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
