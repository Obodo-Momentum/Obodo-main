from django import forms
from .models import Tag, RequestOfferPost, Profile, Comment
from .widgets import MapInput
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Tag, RequestOfferPost, Event, Organization, Member, Profile, Comment
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
# from .widgets import MapInput


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
    tag_names = forms.CharField(label="Tags", help_text="Enter tags separated by spaces.", widget=forms.TextInput(attrs={"class":"form-control"}), required=False)
    post_image = forms.ImageField(required=False)

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
        ]
        widgets = {
            'title' : forms.TextInput(attrs={"class":"form-control"}),
            'post_text' : forms.Textarea(attrs={"class":"form-control"}),
            'category' : forms.Select(attrs={"class":"form-control"}),
            'request_or_offer' : forms.Select(attrs={"class":"form-control"}),
            'post_image' : forms.FileInput(attrs={"class":"form-control-file"}),
            'timeline_start' : DatePickerInput(format='%m/%d/%Y'),
            'timeline_end' : DatePickerInput(format='%m/%d/%Y'),
        }

class ProfileForm(forms.ModelForm):
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

    profile_pic = forms.FileField(label='Upload Your Photo')
    community = forms.ChoiceField(choices=LOCATION_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [
            'profile_pic',
            'community',
        ]

class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = [
            'name',
            'picture',
            'located_at',
            'mission',
        ]
        widgets = {
            'name' : forms.TextInput(attrs={"class":"form-control"}),
            'picture' : forms.FileInput(attrs={"class":"form-control-file"}),
            'located_at' : forms.TextInput(attrs={"class":"form-control"}),
            'mission' : forms.Textarea(attrs={"class":"form-control"}),
        }


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = [
            'username',
        ]
        widgets = {
            'username' : forms.TextInput(attrs={"class":"form-control"}),
        }

class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.
    """
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
    
    required_css_class = 'required'
    community = forms.ChoiceField(choices=LOCATION_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=32, label="Password", help_text="testing", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=32, label="Password Confirmation" , help_text="Enter the same password as before, for verification.", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'community',
            'first_name',
            'last_name',
            ]
        
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        }
# Your password can’t be too similar to your other personal information.
# Your password must contain at least 8 characters.
# Your password can’t be a commonly used password.
# Your password can’t be entirely numeric.

# (<ul> <li>"Your password can’t be too similar to your other personal information."</li> <li>"Your password must contain at least 8 characters."</li> <li>"Your password can’t be a commonly used password."</li> <li>"Your password can’t be entirely numeric."</li> </ul>)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'comment_text'           
        ]

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'host',
            'event_title',
            'event_pic',
            'event_text',
            'attendee',
            'start_date',
            'end_date',
            'event_location',
        ]
        widgets = {
            'start_date' : forms.DateInput(),
            'end_date' : forms.DateInput(),
            'event_pic' : forms.FileInput(),
        }

