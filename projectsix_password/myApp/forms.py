from django import forms
from django.contrib.auth.models import User
from myApp.models import UserProfileInfo

class UserInfoForm(forms.ModelForm):
    """
    Form for creating and updating user information.
    This form is based on the User model and includes fields for username, password, email, first name, and last name.
    """
    password = forms.CharField(widget=forms.PasswordInput, help_text="Enter a strong password.")
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class UserProfileInfoForm(forms.ModelForm):
    """
    Form for creating and updating user profile information.
    This form is based on the UserProfileInfo model and includes fields for profile picture, portfolio site, and bio.
    """
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic', 'portpolio_site', 'bio')
        
        