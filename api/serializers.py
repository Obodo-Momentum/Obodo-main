from rest_framework import serializers
from obodo.models import RequestOfferPost, Comment
from users.models import User

class RequestOfferPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestOfferPost
        fields = (
            'member',
            'post_image',
            'title',
            'post_text',
            'address',
            'location',
            'tags',
            'fulfilled',
            'category',
            'request_or_offer',
            'timeline_start',
            'timeline_end',
            'community',
            'time_stamp',
        )

class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = (
            'original_post',
            'commenter',
            'comment_text',
            'posted_at',
        )

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'date_joined',
        'community',
        'profile_pic',
    )