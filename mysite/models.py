from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from cities_light.models import SubRegion

YEAR_BEGINNING = 2016
YEAR_CURRENT = datetime.today().year


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=255)
    year_opened = models.PositiveSmallIntegerField(default=YEAR_CURRENT,
                                                   validators=[MaxValueValidator(YEAR_CURRENT),
                                                               MinValueValidator(YEAR_BEGINNING)])
    location = models.ForeignKey(SubRegion, on_delete=models.SET_DEFAULT, default='N/A')
    image = models.ImageField(default='default.jpg', upload_to='hotel_pics')

    def __str__(self):
        return self.name
