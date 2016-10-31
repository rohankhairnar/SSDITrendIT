from app.models import UserProfile
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    fullname = forms.CharField(help_text="Please enter your Full Name")
    username = forms.CharField(help_text="Please enter a Username.")
    email = forms.CharField(help_text="Please enter your Email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a Password.")
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text="Re-enter your Password.")

    def clean_password2(self):
            password = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('password2')

            if not password2:
                raise forms.ValidationError("You must confirm your password!")
            if password != password2:
                raise forms.ValidationError("Your passwords do not match, try again!")
            return password2

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ['website', 'picture']
