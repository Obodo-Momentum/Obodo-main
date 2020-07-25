from django.db import models
from django.contrib.auth.models import AbstractUser


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

class Community(models.Model):
    community = models.CharField(max_length=55, choices=LOCATION_CHOICES)


class User(AbstractUser):
    community = models.ForeignKey(to=Community, on_delete=models.CASCADE, related_name='users', null=True, blank=True)




