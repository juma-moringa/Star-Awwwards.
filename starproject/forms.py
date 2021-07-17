
from starproject.models import Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

#signupform
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'user']
     
#update profile form
class UserProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']
