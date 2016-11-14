from mainapp.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.core.validators import validate_email

class UserForm(forms.ModelForm):
    first_name = forms.CharField(help_text="Please enter your Full Name")
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
        fields = ['first_name', 'username', 'email', 'password', 'password2']


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

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