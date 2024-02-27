from django import forms
from . models import Movie

class modelform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','des','year','img']