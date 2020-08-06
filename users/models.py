from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


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
    community = models.CharField(max_length=55, choices=LOCATION_CHOICES)
    profile_pic = ProcessedImageField(upload_to='images', default='default.jpeg',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})



