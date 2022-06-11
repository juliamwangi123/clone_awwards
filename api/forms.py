from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm


class regUserForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'username', 'class':'form-field'}) )

    password1=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-field'})
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':' Confirm Password', 'class':'form-field'})
    )
    check_1=forms.BooleanField()
    check_2=forms.BooleanField()
    class Meta:
        model=User
        fields=['username', 'password1', 'password2', 'check_1',  'check_2']