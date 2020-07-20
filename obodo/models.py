from django.db import models
from users.models import User
import uuid

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

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

class Photo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    photo = models.FileField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="photos", null=True)

class RequestOfferPost(models.Model):
    member = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts", null=True)
    post_image = models.ForeignKey(to=Photo, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=80, null=True, blank=True)
    post_text = models.TextField(max_length=500, help_text="What do you need? What can you give?", null=True, blank=True)
    # location = models.CharField()
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







    