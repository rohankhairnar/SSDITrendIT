
from django.contrib.auth.models import Group
from django import forms
from django.core.validators import validate_email


class TrendForm(forms.ModelForm):
    id = forms.CharField(help_text="Please enter your Full Name")
    name = forms.CharField(help_text="Please enter a Username.")


    class Meta:
        model = Group
        fields = ['id', 'name']