from django import forms
from .models import Tag, RequestOfferPost, Profile
from .widgets import MapInput


# def reverse_tuple_string(location_string):
#     if location_string == "":
#         return location_string
#     args = location_string.split(",")
#     return args[1] + "," + args[0]

# class LocationField(forms.CharField):

#     def __init__(self, *args, **kwargs):
#         map_attrs = kwargs.pop("map_attrs", None)
#         self.widget = MapInput(map_attrs=map_attrs, )

#         super().__init__(*args, **kwargs)
#         self.error_messages = {"required": "Please pick a location", }

#     def to_python(self, value):
#         return super().to_python(reverse_tuple_string(value))

class RequestOfferForm(forms.ModelForm):
    tag_names = forms.CharField(label="Tags", help_text="Enter tags separated by spaces.", widget=forms.TextInput)
    # location = LocationField()
    class Meta:
        model = RequestOfferPost
        fields = [
            'title',
            'post_text',
            'category',
            'request_or_offer',
            'post_image',
            'request_or_offer',
            'timeline_start',
            'timeline_end',
            'location',
        ]
        widgets = {
            'post_text' : forms.Textarea(),
            'timeline_start' : forms.DateInput(),
            'timeline_end' : forms.DateInput(),
        }

class ProfileForm(forms.ModelForm):
    profile_pic = forms.FileField(label='Upload Your Photo')
    class Meta:
        model = Profile
        fields = [
            'profile_pic',
            'community',
        ]