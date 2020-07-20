from django.db import models
from django.contrib.auth.models import AbstractUser
# from obodo.models import Photo

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model

LOCATION_CHOICES = (
    ('Raleigh', 'Raleigh'),
    ('Durham', 'Durham'),
    ('Wake Forest', 'Wake Forest'),
    ('Chapel Hill', 'Chapel Hill'),
    ('Cary', 'Cary'),
    ('Apex/Holly Springs', 'Apex/Holly Springs'),
    ('Garner', 'Garner'),
    ('Clayton', 'Clayton'),
    ('Knightdale/Zebulon', 'Knightdale/Zebulon'),
)

class User(AbstractUser):
    joined_at = models.DateField(auto_now_add=True, blank=True, null=True)
    # user_image = models.ForeignKey(to='obodo.Photo', on_delete=models.CASCADE, default='')
    community = models.CharField(max_length=55, choices=LOCATION_CHOICES, default='')

