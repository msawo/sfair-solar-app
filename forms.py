from django import forms

from . import models

from django.forms import ModelForm
from collection.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'address',)


        
# config this class later
class InstallationForm(forms.ModelForm):
    class Meta:
        model = models.Installation
        fields = [
            'title',
            'order',
            'time_lapsed',
            'description',
        ]


