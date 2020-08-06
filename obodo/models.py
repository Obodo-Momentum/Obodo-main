from django.db import models
from users.models import User
import uuid
from mapbox_location_field.models import LocationField
import datetime
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

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

    CATEGORY_CHOICES = (
    ('kids', 'kids'),
    ('outdoors', 'outdoors'),
    ('services', 'services'),
    ('food', 'food'),
    ('clothing', 'clothing'),
    ('homegoods', 'homegoods'),
    ('furniture', 'furniture'),
    ('books', 'books'),
    )

    member = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts", null=True)
    post_image = ProcessedImageField(upload_to='images', default='',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
    title = models.CharField(max_length=80, null=True, blank=True)
    post_text = models.TextField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    location = LocationField(map_attrs={"center": [0,0], "marker_color": "blue", "track_location_button": True, "geocoder": True}, null=True, blank=True, default='')
    tags = models.ManyToManyField(to=Tag, related_name="posts")
    fulfilled = models.BooleanField(default=False)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    request_or_offer = models.CharField(max_length=50, choices=TYPE_SELECTION)
    timeline_start = models.DateTimeField()
    timeline_end = models.DateTimeField()
    community = models.CharField(max_length=50, null=True, blank=True)
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
            tag = Tag.objects.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)


class Profile(models.Model):
    current_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="profiles", null=True)
    profile_pic = ProcessedImageField(upload_to='images', default='',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
    joined_at = models.DateField(auto_now_add=True, blank=True, null=True)

class Photo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    photo = models.FileField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="photos", null=True)
    

class Comment(models.Model):
    original_post = models.ForeignKey(to=RequestOfferPost, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    commenter = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    comment_text = models.TextField(max_length=1000, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    
class Event(models.Model):
    host = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="events", null=True)
    event_title = models.CharField(max_length=50, null=True, blank=True)
    event_pic = ProcessedImageField(upload_to='images', default='',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
    event_text = models.TextField(max_length=500, null=True, blank=True)
    attendee = models.ManyToManyField(to=User, related_name="attendees")
    start_date = models.DateField(default=datetime.date.today, blank=True)
    end_date = models.DateField(default=datetime.date.today, blank=True)
    event_location = models.CharField(max_length=100, null=True, blank=True)


class Organization(models.Model):
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='creators', null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    picture = ProcessedImageField(upload_to='images', default='',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
    located_at = models.CharField(max_length=200, null=True, blank=True)
    mission = models.TextField(max_length=500, null=True, blank=True)


class Member(models.Model):
    username = models.CharField(max_length=40, null=True, blank=True, help_text='Please enter your username:')
    organization = models.ForeignKey(to=Organization, on_delete=models.CASCADE, related_name='members', null=True)

    def __str__(self):
        return f"{self.username}"

