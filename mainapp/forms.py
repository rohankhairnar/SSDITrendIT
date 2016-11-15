from mainapp.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.core.validators import validate_email

class UserForm(forms.ModelForm):
    first_name = forms.CharField(help_text="Full Name")
    username = forms.CharField(help_text="Username", required=True)
    email = forms.CharField(help_text="Email")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text="Re-enter Password")

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
        fields = ['first_name', 'username', 'email', 'password', 'password2']


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Website", required=False)
    picture = forms.ImageField(help_text="Profile Picture", required=False)

    class Meta:
        model = UserProfile
        fields = ['website', 'picture']



#Form to reset password
class ResetPasswordForm(forms.ModelForm):
    username = forms.CharField(help_text="Username")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Enter new Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text="Confirm Password")

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
        fields = ['username', 'password']


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    contact_email = forms.EmailField(required=True, validators=[validate_email],
                                     widget=forms.TextInput(attrs={'placeholder': 'name@domain.com'}))
    contact_subject = forms.CharField(required=True)
    contact_message = forms.CharField(required=True,
                                      widget=forms.Textarea(attrs={'placeholder': 'Type your message here'}))