from django import forms
from .models import YEAR_CURRENT


class SearchForm(forms.Form):
    year = forms.IntegerField(label='Enter Year', initial=YEAR_CURRENT)
