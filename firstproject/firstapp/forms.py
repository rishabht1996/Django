from django import forms
from .models import Login


class FormName(forms.Form):
    name=forms.CharField(max_length=50)