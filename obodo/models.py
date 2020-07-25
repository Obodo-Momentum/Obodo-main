from django.db import models
from users.models import User
import uuid
from mapbox_location_field.models import LocationField

# Create your models here.


CATEGORY_CHOICES = (
    ('kids', 'kids'),
    ('yard/garden', 'yard/garden'),
    ('odd job', 'odd job'),
    ('skilled labor', 'skilled labor'),
    ('food', 'food'),
    ('clothing', 'clothing'),
    ('homegoods', 'homegoods'),
    ('furniture', 'furniture'),
    ('books', 'books'),
)

TYPE_SELECTION = (
    ('Request', 'Request'),
    ('Offer', 'Offer'),
)

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

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

class RequestOfferPost(models.Model):
    member = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts", null=True)
    post_image = models.ImageField(default='default.jpg')
    title = models.CharField(max_length=80, null=True, blank=True)
    post_text = models.TextField(max_length=500, null=True, blank=True)
    location = LocationField(map_attrs={"center": [0,0], "marker_color": "blue", "track_location_button": True, "geocoder": True}, null=True, blank=True, default='')
    tags = models.ManyToManyField(to=Tag, related_name="posts")
    fulfilled = models.BooleanField(default=False)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    request_or_offer = models.CharField(max_length=50, choices=TYPE_SELECTION)
    timeline_start = models.DateField()
    timeline_end = models.DateField()

    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)
        return " ".join(tag_names)

    def set_tag_names(self, tag_names):
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.object.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)

class Photo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    photo = models.FileField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="photos", null=True)


class Profile(models.Model):
    current_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="profiles", null=True)
    profile_pic = models.ImageField(default='default.jpg')
    joined_at = models.DateField(auto_now_add=True, blank=True, null=True)
    community = models.CharField(max_length=55, choices=LOCATION_CHOICES, default='')


class Comment(models.Model):
    original_post = models.ForeignKey(to=RequestOfferPost, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    commenter = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    comment_text = models.TextField(max_length=1000, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)


class Community (models.Model):
    community  = models.CharField(max_length=55, choices=LOCATION_CHOICES)
    

    