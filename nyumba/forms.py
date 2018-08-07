from .models import NeighbourHood, Profile, Business
from django import forms



class NewAllertForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ['editor', 'pub_date']
        widgets = {
            # 'tags': forms.CheckboxSelectMultiple(),
        }


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class CreateHoodForm(forms.ModelForm):
    class Meta:
        name = NeighbourHood
        exclude = ['admin',]
