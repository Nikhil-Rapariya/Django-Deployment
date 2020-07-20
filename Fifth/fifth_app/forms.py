from django import forms
from django.contrib.auth.models import User
from fifth_app.models import UserProfileInfo

class UserFrom(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model =  User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic','project_link')
