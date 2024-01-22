from django.forms import ModelForm
from django import forms
from .models import Movie, Genre

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year_released', 'genres']
    
    name = forms.CharField()
    year_released = forms.IntegerField()
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )