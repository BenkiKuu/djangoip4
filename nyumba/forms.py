from .models import NeighbourHood, Profile, Business, Allert, Comment
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



class CreateBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['location',]

class CreateAllertForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','post']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
