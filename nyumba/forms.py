from .models import NeighbourHood, Profile, Business
from django import forms





class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
