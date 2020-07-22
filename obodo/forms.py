from django import forms
from .models import Tag, RequestOfferPost


class RequestOfferForm(forms.ModelForm):
    tag_names = forms.CharField(label="Tags", help_text="Enter tags separated by spaces.", widget=forms.TextInput)
    class Meta:
        model = RequestOfferPost
        fields = [
            'title',
            'post_text',
            'category',
            'request_or_offer',
            'image',
            'request_or_offer',
            # 'timeline_start',
            # 'timeline_end',
            # '',


        ]
        