from django.contrib import admin
from .models import RequestOfferPost, Tag, Photo, Event, Organization, Member, Profile, Comment


# Register your models here.
admin.site.register(RequestOfferPost)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(Organization)
admin.site.register(Member)
admin.site.register(Profile)
admin.site.register(Comment)
